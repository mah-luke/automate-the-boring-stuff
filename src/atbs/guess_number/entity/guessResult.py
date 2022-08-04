from dataclasses import dataclass


@dataclass
class GuessResult:
    message: str = None
    correct: bool = None