from pydantic import BaseModel


class ExperimentItem(BaseModel):
    """实验信息"""
    title: str  # 标题
    description: str  # 简介
    limit: int  # 人数上限
    salary: str  # 薪酬
    duration: str  # 时长
    requirements: str  # 报名要求
    tel: int  # 电话号码
    tags: list[str] = []
