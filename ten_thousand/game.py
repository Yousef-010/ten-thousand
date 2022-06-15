import sys
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.bank = Banker()


if __name__ == "__main__":
    game = Game()
    game.play()