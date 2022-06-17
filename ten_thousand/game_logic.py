import random
from collections import Counter


class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(tuple_input):
        """
        this method to calculate_score for every player based on Game Rules
        :param tuple_input:
        :return: score
        """
        score = 0
        nums_rolled = Counter(tuple_input[:6])
        straight = sorted(tuple_input)

        # GET straight
        if straight == [1, 2, 3, 4, 5, 6]:
            score = 1500
            return score

        # GET Ones
        if nums_rolled[1] == 1 or nums_rolled[1] == 2:
            score += 100 * nums_rolled[1]

        # GET Fives
        if nums_rolled[5] == 1 or nums_rolled[5] == 2:
            score += 50 * nums_rolled[5]

        # GET Three pairs
        if nums_rolled[2] == 2 and nums_rolled[3] == 2 and nums_rolled[6] == 2:
            score = 1500
            return score

        if nums_rolled[1] == 2 and nums_rolled[2] == 2 and nums_rolled[3] == 2:
            score = 1500
            return score

        # GET Four ones
        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 4:
                score += 2000
            elif i != 1 and nums_rolled[i] == 4:
                score += i * 200

        # GET Three ones
        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 3:
                score += 1000
            elif i != 1 and nums_rolled[i] == 3:
                score += i * 100

        # GET Six Ones
        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 6:
                score += 4000
            elif i != 1 and nums_rolled[i] == 6:
                score += i * 400

        # GET Five Ones
        for i in range(1, 7):
            if i == 1 and nums_rolled[1] == 5:
                score += 3000
            elif i != 1 and nums_rolled[i] == 5:
                score += i * 300

        return score

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


