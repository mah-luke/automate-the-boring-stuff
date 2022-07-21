from guess_number.controller.controllerConfig import ControllerConfig
from guess_number.controller.guesscontroller import GuessingGameController
from guess_number.handler.advancedGuessHandler import AdvancedGuessHandler


def main():

    controller = GuessingGameController(AdvancedGuessHandler(), ControllerConfig())
    controller.run()


if __name__ == "__main__":
    main()
