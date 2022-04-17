from random import shuffle
from fastapi import FastAPI
from fakers import *
from models import *

app = FastAPI()
experiment_table: list


@app.post("/experiment/new/{item}")
def new_experiment_item(item: ExperimentItem):
    experiment_table.append(item)


@app.get("/experiment/random/{n}")
def get_random_experiment_items(n: int):
    shuffle(experiment_table)
    return experiment_table[:n]
