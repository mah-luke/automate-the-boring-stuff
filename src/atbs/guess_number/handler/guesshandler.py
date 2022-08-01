from atbs.guess_number.entity.guessingGameEntity import GuessingGameEntity
from atbs.guess_number.exception.validationexception import ValidationException


class GuessHandler:

    def __init__(self):
        self.game = None

    def handle(self, guess) -> bool:
        return self.process(self.validate(guess))

    def process(self, validated_guess) -> (bool, str):
        msg = ""
        if validated_guess == self.game.target:
            msg = "Correct number guessed"
            return True
        elif validated_guess < self.game.target:
            msg = "Too low"
        elif validated_guess > self.game.target:
            msg = "Too high"

        return False

    def validate(self, guess: str):
        try:
            casted = int(guess)
        except ValueError:
            raise ValidationException("Input must be an Integer!")

        if casted < self.game.min:
            raise ValidationException(f"Input must be greater than {self.game.min}")

        if casted > self.game.max:
            raise ValidationException(f"Input must be smaller than {self.game.max}")

        return casted

    def setup_handler(self, game: GuessingGameEntity):
        self.game = game





















