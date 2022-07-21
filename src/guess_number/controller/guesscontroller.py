import random

from guess_number.controller.controllerConfig import ControllerConfig
from guess_number.entity.guessingGameEntity import GuessingGameEntity
from guess_number.exception.validationexception import ValidationException
from guess_number.handler.guesshandler import GuessHandler


class GuessingGameController:

    def __init__(self, handler: GuessHandler, config: ControllerConfig):
        # self.game = game
        self.handler = handler
        self.config = config

    def run(self):
        """ Starts up the guessing game which can take one or multiple rounds of numbers to guess."""

        print("Welcome to the guessing game")

        keep_playing = True
        while keep_playing:
            self.run_game()
            keep_playing = True if input("Do you want to continue playing? [y/n] ") in self.config.affirm else False

    def run_game(self):
        """ Execute a game of one random number to guess and return when game is finished """

        self.handler.setup_handler(
            GuessingGameEntity(self.config.min, self.config.max, random.randint(self.config.min, self.config.max), "genericname")
        )
        while True:
            try:
                if self.handler.handle(input(f"Guess a number between {self.config.min} and {self.config.max}: ")):
                    return
            except ValidationException as e:
                print(e)
