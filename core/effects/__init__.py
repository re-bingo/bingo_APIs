from fastapi import APIRouter
import taichi as ti

app = APIRouter()
ti.init(ti.gpu)

__all__ = ["ti", "app"]
