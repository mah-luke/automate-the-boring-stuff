from atbs.guess_number.controller.controllerConfig import ControllerConfig
from atbs.guess_number.controller.guesscontroller import GuessingGameController, GuessingGameControllerConsole
from atbs.guess_number.handler.advancedGuessHandler import AdvancedGuessHandler


def main():

    controller = GuessingGameControllerConsole(AdvancedGuessHandler(), ControllerConfig())
    controller.run()


if __name__ == "__main__":
    main()
