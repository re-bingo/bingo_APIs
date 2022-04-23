from uuid import uuid1
from pydantic import BaseModel
from autoprop import autoprop
from enum import IntEnum


class Sorting(IntEnum):
    smart_descending = 1
    smart_ascending = 2
    cost_descending = 3
    cost_ascending = 4
    duration_descending = 5
    duration_ascending = 6


class NewExperimentItem(BaseModel):
    """实验信息"""
    title: str  # 标题
    description: str  # 简介
    limit: int  # 人数上限
    salary: str  # 薪酬
    duration: str  # 时长
    requirements: str  # 报名要求
    tel: int  # 电话号码
    tags: list[str] = []  # 标签
    start_time: int = 0
    end_time: int = 0


def get_field(field_name: str):
    return (lambda self: self.meta.get(field_name, None),
            lambda self, value: self.meta.__setitem__(field_name, value),
            lambda self: self.meta.pop(field_name))


@autoprop
class Item:
    get_user, set_user, del_user = get_field("user")
    get_title, set_title, del_title = get_field("title")
    get_requirements, set_requirements, del_requirements = get_field("requirements")
    get_description, set_description, del_description = get_field("description")
    get_time_stamp, set_time_stamp, del_time_stamp = get_field("time_stamp")
    get_beginning, set_beginning, del_beginning = get_field("beginning")
    get_duration, set_duration, del_duration = get_field("duration")
    get_deadline, set_deadline, del_deadline = get_field("deadline")
    get_salary, set_salary, del_salary = get_field("salary")
    get_limit, set_limit, del_limit = get_field("limit")
    get_tags, set_tags, del_tags = get_field("tags")

    def __init__(self, kwargs=None):
        self.id = uuid1()
        self.meta = kwargs or {}


@autoprop
class QuestionnaireItem(Item):
    get_body, set_body, del_body = get_field("body")


@autoprop
class ExperimentItem(Item):
    get_tel, set_tel, del_tel = get_field("tel")


@autoprop
class OnlineExperimentItem(ExperimentItem):
    get_period, set_period, del_period = get_field("period")


@autoprop
class OfflineExperimentItem(ExperimentItem):
    pass
