import random


class Player:
    def __init__(self):
        self.human = True
        self.numbers_barrels = 0
        self.card = Card()

    def check(self, number):
        if self.card.numbers.get(number) != None:
            self.card.numbers[number] = 1
        if 0 in self.card.numbers.values():
            return False
        else:
            return True


def pattern_card():
    ###   position_empty_cell = random.sample(range(0, 26), 12)
    ###   position_empty_cell.sort()
    pattern = [1] * 27

    for i in range(0, 3):
        pec = random.sample(range(0, 8), 4)
        pec.sort()
        for ii in pec:
            pattern[ii + 9 * i] = 0
    return pattern


class Card:
    def __init__(self):
        self.numbers = {i: 0 for i in random.sample(range(1, 90), 15)}
        self.pattern = pattern_card()


class Keg:
    def __init__(self):
        self.list_numbers = {i for i in range(1, 90)}

    def pull_keg(self):
        while True:
            num = random.randint(1, 90)
            if num in self.list_numbers:
                self.list_numbers.discard(num)
                return (num)

