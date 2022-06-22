from brotli import MODE_GENERIC, MODE_TEXT, MODE_FONT, Compressor
from starlette.datastructures import Headers, MutableHeaders
from starlette.types import ASGIApp, Message, Receive, Scope, Send


class BrotliMiddleware:
    def __init__(self, app: ASGIApp, minimum_size=512, quality=11, mode=MODE_GENERIC):
        self.app = app
        self.minimum_size = minimum_size
        self.quality = quality
        self.mode = mode

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] == "http":
            headers = Headers(scope=scope)
            if "br" in headers.get("Accept-Encoding", ""):
                responder = BrotliResponder(self.app, self.minimum_size, self.quality)
                await responder(scope, receive, send)
                return

        await self.app(scope, receive, send)


# noinspection PyArgumentList
class BrotliResponder:
    def __init__(self, app: ASGIApp, minimum_size=512, quality=11, mode=MODE_GENERIC):
        self.app = app
        self.minimum_size = minimum_size
        self.send: Send = unattached_send
        self.initial_message: Message = {}
        self.started = False
        self.compressor = Compressor(mode, quality)

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        self.send = send
        await self.app(scope, receive, self.send_with_brotli)

    async def send_with_brotli(self, message: Message):
        message_type = message["type"]
        if message_type == "http.response.start":
            # Don't send the initial message until we've determined how to
            # modify the outgoing headers correctly.
            self.initial_message = message

        elif message_type == "http.response.body" and not self.started:
            self.started = True
            body = message.get("body", b"")
            more_body = message.get("more_body", False)
            if len(body) < self.minimum_size and not more_body:
                # Don't apply Brotli to small outgoing responses
                await self.send(self.initial_message)
                await self.send(message)
            elif not more_body:
                # Standard Brotli response
                body = self.compressor.process(body) + self.compressor.finish()

                headers = MutableHeaders(raw=self.initial_message["headers"])
                headers["Content-Encoding"] = "br"
                headers.add_vary_header("Accept-Encoding")
                headers["Content-Length"] = str(len(body))
                message["body"] = body

                await self.send(self.initial_message)
                await self.send(message)
            else:
                # Initial body in streaming Brotli response.
                headers = MutableHeaders(raw=self.initial_message["headers"])
                headers["Content-Encoding"] = "br"
                headers.add_vary_header("Accept-Encoding")
                del headers["Content-Length"]

                message["body"] = self.compressor.process(body) + self.compressor.flush()

                await self.send(self.initial_message)
                await self.send(message)

        elif message_type == "http.response.body":
            # Remaining body in streaming Brotli response
            body = message.get("body", b"")
            more_body = message.get("more_body", False)

            message["body"] = self.compressor.process(body) + (
                self.compressor.flush() if more_body else self.compressor.finish()
            )

            await self.send(message)


async def unattached_send(message: Message):
    raise RuntimeError("send awaitable not set")  # pragma: no cover
