from random import sample
from fastapi import HTTPException
from diskcache import Deque, Index


class PersistentList:
    def __init__(self, cls):
        self.memo = Deque(directory=f"data/{cls.__name__}")
        self.list = list(self.memo)

    def append(self, new_item):
        self.memo.append(new_item)
        self.list.append(new_item)

    def appendleft(self, new_item):
        self.memo.appendleft(new_item)
        self.list.append(new_item)

    def extend(self, new_items):
        self.memo.extend(new_items)
        self.list.extend(new_items)

    def extendleft(self, new_items):
        self.memo.extendleft(new_items)
        self.list.extend(new_items)

    def clear(self):
        self.memo.clear()
        self.list.clear()

    def sample(self, k):
        return sample(self.list, k)

    def __getitem__(self, item):
        return self.list[item]

    def peek(self):
        return self.memo.peek()

    def peekleft(self):
        return self.memo.peekleft()

    def transact(self):
        return self.memo.transact()

    def __len__(self):
        return len(self.list)


class PersistentDict:
    def __init__(self, cls):
        self.memo = Index(f"data/{cls.__name__}")
        self.dict = dict(self.memo)

    def pop(self, key):
        self.memo.pop(key)
        return self.dict.pop(key)

    def clear(self):
        self.memo.clear()
        self.dict.clear()

    def add(self, value):
        self[value.id] = value

    def __setitem__(self, key, value):
        self.memo[key] = value
        self.dict[key] = value

    def __getitem__(self, item):
        try:
            return self.dict.__getitem__(item)
        except KeyError:
            raise HTTPException(400, f"{item} not in {self.memo.directory}")

    def transact(self):
        return self.memo.transact()

    def __len__(self):
        return len(self.dict)

    def sample(self, k):
        return sample(self.dict.keys(), k)


def field(field_name: str, doc=None):
    return property(lambda self: self.meta.get(field_name, None),
                    lambda self, value: self.meta.__setitem__(field_name, value),
                    lambda self: self.meta.pop(field_name),
                    doc or field_name)


from .experiments import app as experiment_router
from .scales import app as scale_router
from .users import app as user_router
from .fonts import app as font_router

__all__ = ["experiment_router", "scale_router", "user_router", "font_router"]
