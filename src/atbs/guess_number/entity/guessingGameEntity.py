from dataclasses import dataclass


@dataclass
class GuessingGameEntity:
    """ Class for keeping track of the properties and state of the current game """

    min: int = 0
    max: int = 100
    guess_cnt: int = 0
    target: int = None
    name: str = None

    def __init__(self, min, max, target, name):
        self.min = min
        self.max = max
        self.target = target
        self.name = name



