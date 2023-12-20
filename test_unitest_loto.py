import unittest
import random

from loto_classes import Player, Keg

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        pass
    def tearDown(self):
        pass

    def test_init(self):
        self.assertTrue(self.player.human)
        self.assertEqual(self.player.numbers_barrels,0)
        self.assertNotEqual(self.player.card, 0)
        self.assertNotEqual(self.player.card, 0)
        self.assertEqual(len(self.player.card.numbers),15)
        for i in self.player.card.numbers:
            self.assertGreater(i,0)
            self.assertLessEqual(i,90)
        self.assertEqual(len(self.player.card.pattern), 27)
        self.assertEqual(self.player.card.pattern.count(1), 15)
        self.assertEqual(self.player.card.pattern.count(0), 12)
        for i in self.player.card.pattern:
            self.assertGreaterEqual(i,0)
            self.assertLessEqual(i,1)
        self.assertEqual(len(self.player.card.lines), 15)


    def test_check(self):
        i = self.player.card.lines[random.randint(0,14)]
        self.assertEqual(self.player.card.numbers.get(i),0)
        self.assertFalse(self.player.check(i))
        self.assertEqual(self.player.card.numbers.get(i), 1)
        for key in self.player.card.numbers:
            self.player.card.numbers[key] = 1
        self.assertTrue(self.player.check(i))

class TestKeg(unittest.TestCase):
    def setUp(self):
        self.keg = Keg()
        pass
    def tearDown(self):
        pass
    def test_init(self):
        self.assertEqual(len(self.keg.list_numbers),90)
        sum = 0
        for n in self.keg.list_numbers:
            sum += n
        self.assertEqual(sum,4095)
    def test_pull_keg(self):
        num = self.keg.pull_keg()
        self.assertGreater(num, 0)
        self.assertLessEqual(num, 90)
        self.assertIsNot(num,self.keg.list_numbers)


