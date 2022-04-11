import string
from collections import deque
from itertools import chain
from math import sqrt, ceil, floor
from random import shuffle, triangular, choices, randint
from typing import Iterable, Any, Callable


class TruffleShuffle:

    def __init__(self, collection: Iterable[Any]):
        tmp_data = list(collection)
        shuffle(tmp_data)
        self.data = deque(tmp_data)
        self.size = len(self.data)
        self.rotate_size = int(sqrt(self.size))

    def __call__(self) -> Any:
        self.data.rotate(int(triangular(1, self.rotate_size, self.size)))
        selection = self.data[-1]
        if callable(selection):
            return selection()
        else:
            return selection


def generate_uuid(n_len: int):
    n1 = ceil(n_len / 2)
    n2 = floor(n_len / 2)
    prefix = choices(string.ascii_letters, k=n1)
    suffix = map(str, choices(range(0, 9), k=n2))
    uuid_list = list(chain(prefix, suffix))
    shuffle(uuid_list)
    uuid = "".join(uuid_list)
    return uuid


def percent_true(num: int = 50) -> bool:
    return randint(1, 100) <= num


def random_track():
    weights = [40, 30, 0]
    values = ["Web", "DS", "BD"]
    result, *_ = choices(values, weights)
    return result


class NameGenerator:
    random_first_name: Callable[[], str] = TruffleShuffle((
        "Olivia", "Emma", "Ava", "Charlotte", "Sophia", "Amelia", "Isabella", "Mia",
        "Evelyn", "Harper", "Camila", "Gianna", "Abigail", "Luna", "Ella",
        "Elizabeth", "Sofia", "Emily", "Avery", "Mila", "Scarlett", "Eleanor",
        "Madison", "Layla", "Penelope", "Aria", "Chloe", "Grace", "Ellie", "Nora",
        "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas",
        "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob",
        "Logan", "Jackson", "Levi", "Sebastian", "Mateo", "Jack", "Owen",
        "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt",
    ))
    random_last_name: Callable[[], str] = TruffleShuffle((
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
        "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzales",
        "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
        "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
        "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams",
        "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter",
        "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennet",
    ))

    @classmethod
    def generate_name(cls) -> str:
        return f"{cls.random_first_name()} {cls.random_last_name()}"
