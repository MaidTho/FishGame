import unittest

import Main

data_array = []


class Test(unittest.TestCase):
    def test_load(self):
        variable = Main.CheckResults()
        print(variable, not None)
        self.assertTrue(variable, not None)

    def test_main_roll(self):
        DiceRoll = Main.random.randrange(1, 6)
        print(DiceRoll)


if __name__ == '__main__':
    unittest.main()
