# from . import *
import taichi as ti

ti.init()


def new_triangles(width, height):
    return ti.Struct.field(dict(luma1=ti.u8, luma2=ti.u8, reverse=ti.i8), (width, height))


@ti.data_oriented
class TriangleAnimator:
    def __init__(self, width, height, length):
        self.triangles = new_triangles(width, height)
        self.size = length
        self.canvas = ti.field(ti.u8, (height * length, width * length))

    @ti.func
    def render(self):
        triangles, canvas, size = ti.static(self.triangles, self.canvas, self.size)
        triangles: ti.Field
        canvas: ti.Field
        for y, x in canvas:
            i, dx = divmod(x, size)
            j, dy = divmod(y, size)
            triangle: ti.Struct = triangles[i, j]
            if triangle.reverse:
                dx = size - dx - 1
            if dx < dy:
                canvas[y, x] = triangle.luma1
            elif dx > dy:
                canvas[y, x] = triangle.luma2
            else:
                canvas[y, x] = (triangle.luma1 + triangle.luma2) // 2
