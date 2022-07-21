import pytest

from guess_number.controller.guesscontroller import GuessingGameController
from guess_number.handler.guesshandler import GuessHandler


@pytest.fixture
def controller():
    def get_controller(handler: GuessHandler) -> GuessingGameController:
        return GuessingGameController(handler)

    return get_controller
