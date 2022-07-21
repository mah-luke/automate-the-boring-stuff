import pytest as pytest

from guess_number.handler.guesshandler import GuessHandler


def test_run(controller):
    handler = GuessHandler()
    cont = controller()


def test_something_that_involves_user_input(monkeypatch, controller):
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "Mark")

    # go about using input() like you normally would:
    # i = input("What is your name?")
    # assert i == "Mark"
