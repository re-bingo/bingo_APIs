from pydantic import BaseModel
from autoprop import autoprop
from enum import IntEnum
from . import get_field
from uuid import uuid1
from time import time


class Sorting(IntEnum):
    smart_descending = 1
    smart_ascending = 2
    cost_descending = 3
    cost_ascending = 4
    duration_descending = 5
    duration_ascending = 6


class Period(BaseModel):
    start_slot: str
    end_slot: str


class NewExperiment(BaseModel):
    """实验信息"""
    user: str
    title: str = None
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
            user=self.user,
            time_stamp=int(time()),
            title=self.title,
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


@autoprop
class Item:
    """一切项目实例的基类

    - ``user``         用户ID
    - ``title``        标题，查询用
    - ``time_stamp``   时间戳，创建时间
    - ``description``  项目介绍
    - ``requirements`` 对参与者的需求
    - ``release_time`` 发布时间
    - ``start_time``   报名开始时间
    - ``deadline``     报名截止时间
    - ``duration``     实验/问卷的预计持续时间
    - ``salary``       报酬、报酬的形式
    - ``limit``        人数/人次数上限
    - ``tags``         标签的集合（的初始值）
    - ``tel``          联系电话（可选）

    - ``body``         问卷体（问卷特有的属性）
    - ``periods``      时间段（实验特有的属性）（可选）
    """

    get_user, set_user, del_user = get_field("user")
    get_title, set_title, del_title = get_field("title")
    get_time_stamp, set_time_stamp, del_time_stamp = get_field("time_stamp")
    get_description, set_description, del_description = get_field("description")
    get_requirements, set_requirements, del_requirements = get_field("requirements")

    get_release_time, set_release_time, del_release_time = get_field("release_time")
    get_start_time, set_start_time, del_start_time = get_field("start_time")
    get_deadline, set_deadline, del_deadline = get_field("deadline")
    get_duration, set_duration, del_duration = get_field("duration")

    get_salary, set_salary, del_salary = get_field("salary")
    get_limit, set_limit, del_limit = get_field("limit")
    get_tags, set_tags, del_tags = get_field("tags")
    get_tel, set_tel, del_tel = get_field("tel")

    def __init__(self, **kwargs):
        self.id = str(uuid1())
        self.meta = {key: val for key, val in kwargs.items() if val is not None}


@autoprop
class QuestionnaireItem(Item):
    get_body, set_body, del_body = get_field("body")


@autoprop
class ExperimentItem(Item):
    get_periods, set_periods, del_periods = get_field("periods")
