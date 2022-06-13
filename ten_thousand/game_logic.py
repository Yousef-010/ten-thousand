import random


class GameLogic:
    pass

    ###################
    # Calculate score method - Yousef
    ###################

    ###################
    # Roll-Dice method - Shatha
    @staticmethod
    def roll_dice(num):
        # this function take a number of dice rolled as an argument and return a tuple with
        # random numbers in range 1 to 6
        # input : number of rolled dice
        # output : tuple of random numbers between 1 and 6

        return tuple(random.randint(1, 6) for i in range(num))

        # Another solution :
        # dice = []
        # rolling = random.randint(1, 6)
        # for i in range(0, num):
        #     x = rolling
        #     dice.append(x)
        # return dice

    ###################
