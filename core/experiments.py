from . import PersistentList
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from .models import NewExperiment as RealItem, Sorting
from .fakers import NewExperiment as FakeItem

app = APIRouter()

real_items = PersistentList(RealItem)
fake_items = PersistentList(FakeItem)
fake_items.extend(real_items)


@app.get("/fake/sorted/{n}", response_class=ORJSONResponse)
def get_sorted_items(n: int, key: Sorting):
    try:
        if key is Sorting.cost_ascending:
            return sorted(fake_items.list, key=lambda item: item.salary)[:n]
        elif key is Sorting.cost_descending:
            return sorted(fake_items.list, key=lambda item: item.salary, reverse=True)[:n]
        elif key is Sorting.duration_ascending:
            return sorted(fake_items.list, key=lambda item: item.duration)[:n]
        elif key is Sorting.duration_descending:
            return sorted(fake_items.list, key=lambda item: item.duration, reverse=True)[:n]
        elif key is Sorting.smart_ascending:
            return sorted(fake_items.list, key=lambda item: item.limit, reverse=True)[:n]
        elif key is Sorting.smart_descending:
            return sorted(fake_items.list, key=lambda item: item.limit, reverse=False)[:n]
    except RuntimeError as err:
        from fastapi import HTTPException
        raise HTTPException(422, err)


#####################################################################


@app.post("/new/fake", response_class=ORJSONResponse)
async def new_fake_experiment_item(item: FakeItem):
    """
    add a fake ExperimentItem to the fake database
    - the unfilled parameters will be default(fake) values
    """
    fake_items.append(item.to_item())
    return item.to_item().id


@app.delete("/fake", response_class=ORJSONResponse)
async def clear_all_fake_experiments():
    """clear the fake database"""
    return fake_items.clear()


@app.get("/fake/random/{n}", response_class=ORJSONResponse)
async def get_random_fake_items(n: int):
    """
    get many fake experimentItems as you want

    in case you require more than you posted,
    I promise you get something random rather than errors
    """
    for _ in range(n - len(fake_items)):
        await new_fake_experiment_item(FakeItem())
    return fake_items.sample(n)


#####################################################################


@app.post("/new", response_class=ORJSONResponse)
async def new_experiment_item(item: RealItem):
    real_items.append(item.to_item())
    return item.to_item().id


@app.delete("/", response_class=ORJSONResponse)
async def clear_all_experiments():
    return real_items.clear()


@app.get("/random/{n}", response_class=ORJSONResponse)
async def get_random_items(n: int):
    return real_items.sample(n)
