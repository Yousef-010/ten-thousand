
try:
    from game_logic import GameLogic
    from banker import Banker
    import sys
except ImportError:
    from .game_logic import GameLogic
    from .banker import Banker
    import sys


class Game:
    def __init__(self):
        self.round = 1
        self.dice = 6
        self.flag = False
        self.banker = Banker()

    def play(self, roller=GameLogic.roll_dice):
        self.roller = roller
        self.welcome()
        while self.flag:
            print(f'Rolling {self.dice} dice...')
            self.formatted_roll()
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')
            if user_answer == 'q':
                self.quit()
            if user_answer != 'q':
                score, dices_shelved = self.roll_and_get_score(user_answer)
                self.banker.shelf(score)
                self.dice -= dices_shelved

                print(f'You have {self.banker.shelved} unbanked points and {self.dice} dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')

                user_answer = input('> ')
                if user_answer == 'q':
                    self.quit()
                if user_answer == 'b':
                    print(f'You banked {self.banker.shelved} points in round {self.round}')
                    self.banker.bank()
                    print(f'Total score is {self.banker.balance} points')
                    self.round += 1
                    print(f'Starting round {self.round}')
                    self.dice = 6

    def formatted_roll(self):
        roller_input = ' '.join(map(str, (self.roller(self.dice))))
        print(f'*** {roller_input} ***')

    def roll_and_get_score(self, user_answer):
        dices = tuple([int(x) for x in user_answer])
        dices_shelved = len(dices)
        score = GameLogic.calculate_score(dices)
        return score, dices_shelved

    def welcome(self):
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            self.game_over()
        else:
            print(f'Starting round {self.round}')
            self.flag = True

    def quit(self):
        print(f'Thanks for playing. You earned {self.banker.balance} points')
        sys.exit()

    @staticmethod
    def game_over():
        print('OK. Maybe another time')


if __name__ == '__main__':
    game = Game()
    game.play()