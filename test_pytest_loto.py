import random

import pytest
from loto_classes import Player, Keg
class TestPlayer:
    def setup(self):
        self.player = Player()
        pass
    def teardown(self):
        pass

    def test_init(self):
        assert self.player.human == True
        assert self.player.numbers_barrels == 0
        assert self.player.card != 0
        assert len(self.player.card.numbers) == 15
        for i in self.player.card.numbers:
            assert  i > 0 and i < 91
        assert len(self.player.card.pattern) == 27
        assert self.player.card.pattern.count(1) == 15
        assert self.player.card.pattern.count(0) == 12
        for i in self.player.card.pattern:
            assert  i == 0 or i == 1
        assert len(self.player.card.lines) == 15

    def test_check(self):
        i = self.player.card.lines[random.randint(0,14)]
        assert self.player.card.numbers.get(i) == 0
        assert self.player.check(i) == False
        assert self.player.card.numbers.get(i) == 1
        for key in self.player.card.numbers:
            self.player.card.numbers[key] = 1
        assert self.player.check(i) == True

class TestKeg:
    def setup(self):
        self.keg = Keg()
        pass
    def teardown(self):
        pass
    def test_init(self):
        assert len(self.keg.list_numbers) == 90
        sum = 0
        for n in self.keg.list_numbers:
            sum += n
        assert sum == 4095

    def test_pull_keg(self):
        num = self.keg.pull_keg()
        assert num > 0 and num <91
        assert num not in self.keg.list_numbers