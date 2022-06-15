import sys
from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.bank = Banker()

    die = 6
    round_num = 0
    score = 0
    balance = 0

    def rounds(self, round_num, die, roller, score, balance):
        round_num += 1
        print(f'Starting round {round_num}')
        print(f'Rolling {die} dice...')
        roller_input = ' '.join(map(str, (roller(die))))
        print(f'*** {roller_input} ***')
        print('Enter dice to keep, or (q)uit:')
        response = input('> ')

        if response == 'q':
            print(f'Thanks for playing. You earned {balance} points')

        else:
            keep_die = tuple([int(var) for var in str(response)])
            die = die - len(keep_die)
            score += GameLogic.calculate_score(keep_die)
            print(f'You have {score} unbanked points and {die} dice remaining')
            print('(r)oll again, (b)ank your points or (q)uit:')
            response = input('> ')

            if response == 'b':
                self.bank.shelf(score)
                balance += score
                print(f'You banked {score} points in round {round_num}')
                print(f'Total score is {balance} points')
                die = 6
                score = 0
                self.rounds(round_num, die, roller, score, balance)

            # if response == 'r':

    def play(self, roller=GameLogic.roll_dice):
        round_num = 0
        die = 6
        balance = 0
        score = 0
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        response = input('> ')
        if response == 'n':
            print('OK. Maybe another time')

        if response == 'y':
            self.rounds(round_num, die, roller, balance, score)


if __name__ == "__main__":
    game = Game()
    game.play()
