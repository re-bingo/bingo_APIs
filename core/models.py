from pydantic import BaseModel
from typing import Union
from enum import IntEnum
from uuid import uuid1
from time import time
from . import field


class Sorting(IntEnum):
    smart_descending = 1
    smart_ascending = 2
    cost_descending = 3
    cost_ascending = 4
    duration_descending = 5
    duration_ascending = 6


class status(IntEnum):
    before_apply = 0
    reviewing = 1
    failed = 2
    approved = 3


class Period(BaseModel):
    start_slot: str
    end_slot: str


class UserList(BaseModel):
    users: list[str] = []
    sexes: str = None
    universities: list[str] = []


class BlackList(BaseModel):
    pass


class WhiteList(BaseModel):
    pass


class Selector(BaseModel):
    selectors: list[Union[BlackList, WhiteList]]
    next: "Selector"

    def __bool__(self):
        return bool(self.selectors)

    def visible_to(self, user_id):
        _ = self, user_id
        return NotImplemented


class NewExperiment(BaseModel):
    """实验信息"""
    title: str = None
    logic: Selector = None
    author: str
    visible: bool = False
    description: str = None
    requirements: str = None
    release_time: int = None
    start_time: int = None
    deadline: int = None
    limit: int = None
    salary: str = None
    duration: str = None
    tel: int = None
    tags: list[str] = []
    periods: list[Period] = []

    def to_item(self):
        return ExperimentItem(
            author=self.author,
            logic=self.logic,
            timestamp=int(time()),
            title=self.title,
            visible=self.visible,
            description=self.description,
            requirements=self.requirements,
            release_time=self.release_time,
            salary=self.salary,
            start_time=self.start_time,
            deadline=self.deadline,
            duration=self.duration,
            tags=self.tags,
            limit=self.limit,
            tel=self.tel,
            periods=self.periods
        )


class Item:
    title = field("title", "标题")
    logic = field("logic", "权限")
    author = field("author", "用户ID")
    status = field("status", "审核状态")
    visible = field("visible", "对外可见")
    timestamp = field("timestamp", "创建时间")
    description = field("description", "描述")
    requirements = field("requirements", "要求")
    release_time = field("release_time", "发布时间")
    start_time = field("start_time", "报名起始时间")
    deadline = field("deadline", "报名结束时间")
    duration = field("duration", "持续时间")
    salary = field("salary", "报酬方式")
    limit = field("limit", "人数上限")
    tags = field("tags", "标签集")
    tel = field("tel", "电话")

    def __init__(self, **kwargs):
        self.id = str(uuid1())
        self.meta = {key: val for key, val in kwargs.items() if val is not None}


class QuestionnaireItem(Item):
    body = field("body", "问卷体")

    @property
    def complete(self):
        return self.visible and all((
            self.title, self.description, self.salary, self.body,
            self.limit, self.duration, self.deadline
        ))


class ExperimentItem(Item):
    periods = field("periods", "时间段")

    @property
    def complete(self):
        return self.visible and all((
            self.title, self.description, self.salary,
        ))
