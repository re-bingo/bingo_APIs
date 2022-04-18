from random import shuffle
from fastapi import FastAPI
from diskcache import Deque
from fastapi.responses import RedirectResponse
from core.fakers import ExperimentItem

app = FastAPI()

doc = RedirectResponse("/redoc")


@app.get("/")
def home_page():
    """redirect you to the document page"""
    return doc


class ExperimentAPI:
    experiment_table = Deque(directory="data")
    experiment_list = list(experiment_table)

    @staticmethod
    @app.post("/experiment/new")
    def new_experiment_item(item: ExperimentItem):
        ExperimentAPI.experiment_table.append(item)
        ExperimentAPI.experiment_list.append(item)

    @staticmethod
    @app.put("/experiment/clear")
    def clear_all_experiments():
        ExperimentAPI.experiment_table.clear()
        ExperimentAPI.experiment_list.clear()

    @staticmethod
    @app.get("/experiment/random/{n}")
    def get_random_experiment_items(n: int):
        shuffle(ExperimentAPI.experiment_list)
        return ExperimentAPI.experiment_list[:n]

    @staticmethod
    @app.get("/fake_experiment")
    def get_random_experiment_item():
        new_item = ExperimentItem()
        ExperimentAPI.new_experiment_item(new_item)
        return new_item
