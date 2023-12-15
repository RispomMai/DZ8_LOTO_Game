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
    pattern = [1] * 27
    for i in range(0, 3):
        pec = random.sample(range(0, 8), 4)
        pec.sort()
        for ii in pec:
            pattern[ii + 9 * i] = 0
    return pattern

def define_lines_card(s):
    list_values =[]
    for i in range(0,3):
        ss = s[i*5:i*5+5]
        ss.sort()
        list_values += ss
    return list_values

class Card:
    def __init__(self):
        self.numbers = {i: 0 for i in random.sample(range(1, 90), 15)}
        self.pattern = pattern_card()
        self.lines = define_lines_card(list(self.numbers.keys()))


class Keg:
    def __init__(self):
        self.list_numbers = {i for i in range(1, 90)}

    def pull_keg(self):
        while True:
            num = random.randint(1, 90)
            if num in self.list_numbers:
                self.list_numbers.discard(num)
                return (num)

