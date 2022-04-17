from . import faker
from .. import models
from random import choice, randrange

possible_titles = open("titles.txt").read().strip().split()
possible_tags = open("tags.txt").read().strip().split()


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
    def fake_tags():
        return choice(possible_tags)
