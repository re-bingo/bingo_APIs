from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ExperimentItem(BaseModel):
    """实验信息"""
    title: str         # 标题
    description: str   # 简介
    limit: int         # 人数上限
    salary: str        # 薪酬
    duration: str      # 时长
    requirements: str  # 报名要求
    tel: int           # 电话号码


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
