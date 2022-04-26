from . import PersistentDict, get_field
from functools import cached_property
from uuid import uuid5, NAMESPACE_DNS
from cachetools.func import ttl_cache
from autoprop import autoprop
from fastapi import APIRouter
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

    def to_user(self):
        return User(self)


@autoprop
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

    get_name, set_name, del_name = get_field("name")
    get_sex, set_sex, del_sex = get_field("sex")
    get_tel, set_tel, del_tel = get_field("tel")
    get_university, set_university, del_university = get_field("university")
    get_number, set_number, del_number = get_field("number")

    def check(self):
        return self.name and self.sex and self.tel and self.university and self.number


User.users = PersistentDict(User)
app = APIRouter()


@app.get("/code2id")
async def get_id_from_code(code: str):
    return WeChatUser(code).id


@app.get("/code2openid")
async def get_openid_from_code(code: str):
    return WeChatUser(code).openid


@app.get("/code2unionid")
async def get_unionid_from_code(code: str):
    return WeChatUser(code).unionid


@app.get("/id2openid")
async def get_openid_from_id(id: str):
    return User.users[id].openid


@app.get("/id2unionid")
async def get_unionid_from_id(id: str):
    return User.users[id].unionid


@app.get("/meta")
async def get_user_information(id: str):
    return User.users[id].meta


@app.put("/register/{id}")
async def update_user_information(id: str, data: dict):
    User.users[id].meta.update(data)


@app.get("/all")
async def get_all_users():
    return list(User.users.dict.keys())


@app.delete("/")
async def massacre():
    """# 该操作会立即删除所有用户！"""
    User.users.clear()
