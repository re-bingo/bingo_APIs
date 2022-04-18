from random import shuffle
from fastapi import FastAPI
from core.fakers import ExperimentItem

# from core.models import ExperimentItem

app = FastAPI()
experiment_table: list = []


@app.post("/experiment/new")
def new_experiment_item(item: ExperimentItem):
    experiment_table.append(item)


@app.get("/test_experiment")
def get_random_experiment_item():
    return ExperimentItem()


@app.get("/experiment/random/{n}")
def get_random_experiment_items(n: int):
    shuffle(experiment_table)
    return experiment_table[:n]
