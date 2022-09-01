import uuid
from collections import deque
from math import sqrt
from random import shuffle, triangular, choices, randint
from typing import Any, Callable, List


class TruffleShuffle:

    def __init__(self, collection: List[Any]):
        shuffle(collection)
        self.data = deque(collection)

    def __call__(self) -> Any:
        size = len(self.data)
        pivot = sqrt(size)
        rotate = size / 2
        self.data.rotate(int(triangular(1, rotate, pivot)))
        return self.data[-1]


def random_uuid() -> str:
    return str(uuid.uuid4())


def percent_true(num: int = 50) -> bool:
    return randint(1, 100) <= num


def random_track() -> str:
    tracks = {
        "Web": 60,
        "DS": 40,
        "BD": 0,
    }
    track, *_ = choices(*zip(*tracks.items()))
    return track


random_first_name: Callable[[], str] = TruffleShuffle([
    "Olivia", "Emma", "Ava", "Charlotte", "Sophia", "Amelia", "Isabella", "Mia",
    "Evelyn", "Harper", "Camila", "Gianna", "Abigail", "Luna", "Ella",
    "Elizabeth", "Sofia", "Emily", "Avery", "Mila", "Scarlett", "Eleanor",
    "Madison", "Layla", "Penelope", "Aria", "Chloe", "Grace", "Ellie", "Nora",
    "Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas",
    "Henry", "Alexander", "Mason", "Michael", "Ethan", "Daniel", "Jacob",
    "Logan", "Jackson", "Levi", "Sebastian", "Mateo", "Jack", "Owen",
    "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt",
])


random_last_name: Callable[[], str] = TruffleShuffle([
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzales",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark",
    "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Allen", "King",
    "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams",
    "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter",
    "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennet",
])


def random_name() -> str:
    return f"{random_first_name()} {random_last_name()}"
