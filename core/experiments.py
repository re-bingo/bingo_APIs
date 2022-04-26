from . import PersistentList
from fastapi import APIRouter
from .models import NewExperiment as RealItem
from .fakers import NewExperiment as FakeItem

app = APIRouter()

real_items = PersistentList(RealItem)
fake_items = PersistentList(FakeItem)
fake_items.extend(real_items)


@app.post("/new/fake", tags=["faking"])
async def new_fake_experiment_item(item: FakeItem):
    """
    add a fake ExperimentItem to the fake database
    - the unfilled parameters will be default(fake) values
    """
    return fake_items.append(item.to_item())


@app.delete("/fake", tags=["faking"])
async def clear_all_fake_experiments():
    """clear the fake database"""
    return fake_items.clear()


@app.get("/fake/random/{n}", tags=["faking"])
async def get_random_fake_items(n: int):
    """
    get many fake experimentItems as you want

    in case you require more than you posted,
    I promise you get something random rather than errors
    """
    fake_items.shuffle()
    for _ in range(n - len(fake_items)):
        await new_fake_experiment_item(FakeItem())
    return fake_items[:n]


#####################################################################


@app.post("/new")
async def new_experiment_item(item: RealItem):
    return real_items.append(item.to_item())


@app.delete("/")
async def clear_all_experiments():
    return real_items.clear()


@app.get("/random/{n}")
async def get_random_items(n: int):
    real_items.shuffle()
    return real_items[:n]
