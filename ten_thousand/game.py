

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
        self.roller = None
        self.round = 1
        self.dice = 6
        self.flag = False
        self.flag_ch = True
        self.dices_shelved = 0
        self.banker = Banker()

    def play(self, roller=GameLogic.roll_dice):
        self.roller = roller
        self.welcome()
        while self.flag:
            print(f'Rolling {self.dice} dice...')
            print_roll = self.formatted_roll()
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')
            if user_answer == 'q':
                self.quit()
            if user_answer != 'q':
                self.check_cheaters(print_roll,  user_answer)
                if self.flag_ch:
                    score = self.roll_and_get_score(user_answer)[0]
                    self.banker.shelf(score)
                self.flag_ch = True
                self.dice -= self.dices_shelved

                print(f'You have {self.banker.shelved} unbanked points and {self.dice} dice remaining')
                print('(r)oll again, (b)ank your points or (q)uit:')
                if self.dice == 0:
                    self.dice = 6
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
        self.check_zilch(roller_input)
        return roller_input

    def check_zilch(self, roller_input):
        value = (tuple(map(int, ''.join(roller_input.split(' ')))))
        if GameLogic.calculate_score(value) == 0:
            self.zilch()
        return value

    def roll_and_get_score(self, user_answer):
        dices = tuple([int(x) for x in user_answer])
        self.dices_shelved = len(dices)
        score = GameLogic.calculate_score(dices)
        return score,  dices

    def zilch(self):
        self.banker.clear_shelf()
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f"You banked {self.banker.balance} points in round {self.round}")
        print(f"Total score is {self.banker.balance} points")
        self.dice = 6
        self.round += 1
        print(f'Starting round {self.round}')
        print(f'Rolling {self.dice} dice...')
        self.formatted_roll()

    @staticmethod
    def die(user_answer):
        die = tuple([int(x) for x in user_answer])
        return die

    def check_cheaters(self, roller_input, user_answer):
        value = (tuple(map(int, ''.join(roller_input.split(' ')))))
        dices = self.die(user_answer)
        # common_ele = set(value) & set(dices)
        common_ele = []
        for element1 in value:
            if element1 in dices:
                common_ele.append(element1)

        if len(tuple(common_ele)) < len(dices):
            self.flag_ch = False
            print('Cheater!!! Or possibly made a typo...')
            self.dice = 6
            value = ' '.join(map(str, value))
            print(f'*** {value} ***')
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')
            score = self.roll_and_get_score(user_answer)[0]
            self.banker.clear_shelf()
            self.banker.shelf(score)

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