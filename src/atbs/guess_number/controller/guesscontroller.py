import random

from atbs.guess_number.controller.controllerConfig import ControllerConfig
from atbs.guess_number.entity.guessResult import GuessResult
from atbs.guess_number.entity.guessingGameEntity import GuessingGameEntity
from atbs.guess_number.exception.validationexception import ValidationException
from atbs.guess_number.handler.guesshandler import GuessHandler


class GuessingGameController:

    def __init__(self, handler: GuessHandler, config: ControllerConfig):
        self.handler = handler
        self.config = config

    def start_new_game(self) -> GuessingGameEntity:
        """ Start a new game """
        new_game = GuessingGameEntity(
            self.config.min,
            self.config.max,
            random.randint(self.config.min, self.config.max),
            "genericGame"
        )
        self.handler.setup_handler(new_game)

    def guess(self, value: str) -> GuessResult:
        """  """
        return self.handler.handle(value)


class GuessingGameControllerConsole(GuessingGameController):

    def run(self):
        """ Starts up the guessing game which can take one or multiple rounds of numbers to guess."""

        print("Welcome to the guessing game")

        keep_playing = True
        while keep_playing:
            self.run_game()
            keep_playing = True if input("Do you want to continue playing? [y/n] ") in self.config.affirm else False

    def run_game(self):
        """ Execute a game of one random number to guess and return when game is finished """

        self.start_new_game()
        while True:
            try:
                result = self.guess(input(f"Guess a number between {self.config.min} and {self.config.max}: "))
                print(result.message, end="")
                if result.correct:
                    return
            except ValidationException as e:
                print(e)
