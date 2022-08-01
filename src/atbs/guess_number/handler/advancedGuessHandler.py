from atbs.guess_number.entity.guessingGameEntity import GuessingGameEntity
from atbs.guess_number.handler.guesshandler import GuessHandler


class AdvancedGuessHandler(GuessHandler):

    def __init__(self):
        super().__init__()
        self.highest = None
        self.lowest = None

    def handle(self, guess):
        validated_guess = self.validate(guess)
        res = self.process(validated_guess)

        if not res:
            # update guessing limits according to current guess
            if self.game.target > validated_guess >= self.lowest:
                self.lowest = validated_guess + 1
            if self.highest >= validated_guess > self.game.target:
                self.highest = validated_guess - 1

            print(f"Next guess recommended: {self.get_optimal_guess()}")

        return res

    def get_optimal_guess(self):
        return int((self.highest - self.lowest) / 2) + self.lowest

    def setup_handler(self, game: GuessingGameEntity):
        super().setup_handler(game)
        self.highest = game.max
        self.lowest = game.min
