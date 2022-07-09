"""
this is where to generate scales.pkl, 
which is what I did in 
"https://github.com/CNSeniorious000/scale_scraper".
"""

from functools import cached_property, cache
from bs4 import BeautifulSoup
from rich import *
from httpx import Client

baseurl = "https://www.obhrm.net"


class OBHRM:
    def __init__(self):
        self.current_page: BeautifulSoup = self.html("/index.php/栏目:研究量表")

    @cached_property
    def client(self):
        return Client(follow_redirects=True, http2=True)

    @cache
    def get(self, url):
        return self.client.get(url)

    @cache
    def html(self, url):
        return BeautifulSoup(self.get(baseurl + url).text, "lxml")

    def turn_to_next_page(self):
        tag = (
            self.current_page
            .find_all("div")[2].find_all("div")[4].find_all("div")[3]
            .div.div.find_all("a")[-1]
        )
        assert tag.text == "下一页"
        self.current_page = self.html(tag["href"])

    @property
    def groups(self) -> list[BeautifulSoup]:
        return (
            self.current_page
            .find_all("div")[2].find_all("div")[4].find_all("div")[3]
            .find_all("div")[4:]
        )

    @staticmethod
    @cache
    def get_paths(group: BeautifulSoup) -> list[str]:
        return [li.a["href"] for li in group.find_all("li")]

    @cached_property
    def all_paths(self) -> list[str]:
        paths = sum(map(self.get_paths, self.groups), [])
        self.turn_to_next_page()
        paths.extend(sum(map(self.get_paths, self.groups), []))
        self.turn_to_next_page()
        paths.extend(sum(map(self.get_paths, self.groups), []))
        return paths

    def parse_page(self, path):
        soup: BeautifulSoup = self.html(path)
        title = soup.head.title.text.removesuffix(" - OBHRM百科")
        toc: BeautifulSoup = soup.body.find_all("div")[2].find_all("div")[3].find_all("div")[3].div

        content = {}
        paragraphs = None
        for tag in toc.find_next_siblings():
            tag: BeautifulSoup

            if tag.name == "h2":
                new_subtitle = tag.text
                content[new_subtitle] = paragraphs = []
            elif tag.name == "p":
                paragraphs.append(tag.text.strip())
                if tag.a is not None:
                    paragraphs.append(baseurl + self.follow_download_link(tag.a["href"]))
            elif tag.name == "pre":
                paragraphs.append(tag.text.strip())
            else:
                print(f"\n{tag.prettify() = !s}\n{tag.text.strip() = !s}\n")
                paragraphs.append(tag.text.strip())

        return title, content

    def follow_download_link(self, url: str):
        if url.startswith("/index.php/"):
            return self.html(url).select_one(".internal")["href"]
        else:
            return url


if __name__ == '__main__':
    print(len(OBHRM().all_paths))  # 533
