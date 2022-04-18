from . import faker
from .. import models
from time import time
from random import choice, randrange, shuffle

path = __package__.replace(".", "/")

possible_titles = open(f"{path}/titles.txt").read().strip().split()
possible_tags = open(f"{path}/tags.txt").read().strip().split()


class ExperimentItem(models.ExperimentItem):
    @staticmethod
    def fake_title():
        return choice(possible_titles)

    @staticmethod
    def fake_description(n=None):
        return "\n".join(faker.paragraphs(n or randrange(4, 15)))

    @staticmethod
    def fake_limit(min_=None, max_=None):
        return randrange(min_ or 0, max_ or 40)

    @staticmethod
    def fake_salary(min_=None, max_=None):
        return str(randrange(min_ or 1, max_ or 100))

    @staticmethod
    def fake_duration(min_=None, max_=None):
        return str(randrange(min_ or 5, max_ or 60))

    @staticmethod
    def fake_requirements(n=None):
        return ExperimentItem.fake_description(n)

    @staticmethod
    def fake_tel():
        return faker.phone_number()

    @staticmethod
    def fake_tags(n=None):
        shuffle(possible_tags)
        return possible_tags[:n or randrange(2, 7)]

    def __init__(self, **kwargs):
        params = {
            "title": self.fake_title(),
            "description": self.fake_description(),
            "limit": self.fake_limit(),
            "salary": self.fake_salary(),
            "duration": self.fake_duration(),
            "requirements": self.fake_requirements(),
            "tel": self.fake_tel(),
            "tags": self.fake_tags(),
            "start_time": (now := time()),
            "end_time": now + 24 * 60 * 60
        }
        params.update(kwargs)
        super().__init__(**params)
