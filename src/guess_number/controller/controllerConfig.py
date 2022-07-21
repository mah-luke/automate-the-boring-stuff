from dataclasses import dataclass


@dataclass
class ControllerConfig:
    min = 0
    max = 100
    affirm = ["y"]
