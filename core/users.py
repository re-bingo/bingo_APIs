from functools import cached_property
from uuid import uuid5, NAMESPACE_DNS
from cachetools.func import ttl_cache
from fastapi import APIRouter
from . import PersistentDict
from .secret import *
import requests


@ttl_cache(ttl=30)
def code2session(code: str) -> dict:
    return requests.get(
        "https://api.weixin.qq.com/sns/jscode2session?"
        f"appid={appId}&secret={appSecret}&js_code={code}&grant_type=authorization_code"
    ).json()


class WeChatUser:
    def __init__(self, code):
        self.meta = code2session(code)

    @property
    def openid(self) -> str:
        return self.meta["openid"]

    @property
    def session_id(self) -> str:
        return self.meta["session_key"]

    @property
    def unionid(self) -> str:
        return self.meta["unionid"]

    @property
    def errcode(self) -> int:
        return self.meta["errcode"]

    @property
    def errmsg(self) -> str:
        return self.meta["errmsg"]

    @cached_property
    def id(self):
        return uuid5(NAMESPACE_DNS, self.openid)


class User:
    users: PersistentDict

    def __new__(cls, wechat_user: WeChatUser, **kwargs):
        try:
            user: User = cls.users[wechat_user.id]
            user.meta.update(kwargs)
        except KeyError:
            user = object.__new__(cls)
            cls.users[wechat_user.id] = user
        return user

    def __init__(self, wechat_user: WeChatUser, **kwargs):
        self.meta = kwargs
        self.id = wechat_user.id
        self.openid = wechat_user.openid
        self.unionid = wechat_user.unionid


User.users = PersistentDict(User)
app = APIRouter()


@app.get("/code2id")
def get_id_from_code(code: str):
    return User(WeChatUser(code)).id


@app.get("/code2openid")
def get_openid_from_code(code: str):
    return WeChatUser(code).openid


@app.get("/code2unionid")
def get_unionid_from_code(code: str):
    return WeChatUser(code).unionid


@app.get("/id2openid")
def get_openid_from_id(id: str):
    return User.users[id].openid


@app.get("/id2unionid")
def get_unionid_from_id(id: str):
    return User.users[id].unionid


@app.get("/meta")
def get_user_meta(id: str):
    return User.users[id].meta


@app.put("/register/{id}")
def update_user_information(id: str, data: dict):
    User.users[id].meta.update(data)


@app.get("/all")
def get_all_users():
    return User.users.dict.keys()


@app.delete("/")
def massacre():
    """# 该操作会立即删除所有用户！"""
    User.users.clear()
