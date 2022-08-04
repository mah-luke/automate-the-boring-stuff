from atbs.guess_number.entity.guessResult import GuessResult
from atbs.guess_number.entity.guessingGameEntity import GuessingGameEntity
from atbs.guess_number.exception.validationexception import ValidationException


class GuessHandler:

    def __init__(self):
        self.game = None

    def handle(self, guess) -> GuessResult:
        return self.process(self.validate(guess))

    def process(self, validated_guess) -> GuessResult:
        result = GuessResult()
        if validated_guess == self.game.target:
            result.message = "Correct number guessed\n"
            result.correct = True
        else:
            if validated_guess < self.game.target:
                result.message = "Too low\n"
            elif validated_guess > self.game.target:
                result.message = "Too high\n"
            result.correct = False

        return result

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





















