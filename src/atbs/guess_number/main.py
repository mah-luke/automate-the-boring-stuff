from atbs.guess_number.controller.controllerConfig import ControllerConfig
from atbs.guess_number.controller.guesscontroller import GuessingGameController
from atbs.guess_number.handler.advancedGuessHandler import AdvancedGuessHandler


def main():

    controller = GuessingGameController(AdvancedGuessHandler(), ControllerConfig())
    controller.run()


if __name__ == "__main__":
    main()
