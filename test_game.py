import unittest
from dice import Dice
from win_validator import WinChecker

class TestDice(unittest.TestCase):
    """
    Tests for the Dice object.
    """

    def test_dice(self):
        """
        Test that dice successfully created 
        """
        test_die = Dice()
        roll = test_die.get_num()  # since dice have not been rolled, empty list
        self.assertEqual(len(roll), 0)

    def test_roll(self):
        """
        Test that there was a succesful roll of 5 die.
        """
        test_die = Dice()
        test_die.roll_dice()
        roll = test_die.get_num()
        self.assertEqual(len(roll), 5)

class TestWinChecker(unittest.TestCase):
    """
    Tests to verify that scores are accurately calculated.
    """

    def test_all_ones(self):
        """
        Test a score of five 1s rolled.
        Score should be equal to 1200.
        """
        test_rolls = {1:5}
        test_wins = WinChecker(test_rolls)
        test_wins.verify_wins()
        test_scores = test_wins.get_score()
        self.assertEqual(test_scores, 1200)

    def test_triple_fives(self):
        """
        Test a score of three 5s and two non-scoring numbers.
        Score should be equal to 500.
        """
        test_rolls = {5:3, 2:2}
        test_wins = WinChecker(test_rolls)
        test_wins.verify_wins()
        test_scores = test_wins.get_score()
        self.assertEqual(test_scores, 500)

    def test_no_score(self):
        """
        Test a score of no point-winning numbers rolled.
        Score should be equal to 0.
        """
        test_rolls = {3:2, 2:2, 4:1}
        test_wins = WinChecker(test_rolls)
        test_wins.verify_wins()
        test_scores = test_wins.get_score()
        self.assertEqual(test_scores, 0)

    def test_single_one(self):
        """
        Test a score of a single 1 rolled.
        Score should be equal to 100.
        """
        test_rolls = {3:2, 2:2, 1:1}
        test_wins = WinChecker(test_rolls)
        test_wins.verify_wins()
        test_scores = test_wins.get_score()
        self.assertEqual(test_scores, 100)

    def test_multiple_scores(self):
        """
        Test a score of triple 4s, single 1, single 5.
        Score should be equal to 550.
        """
        test_rolls = {4:3, 1:1, 5:1}
        test_wins = WinChecker(test_rolls)
        test_wins.verify_wins()
        test_scores = test_wins.get_score()
        self.assertEqual(test_scores, 550)

if __name__ =="__main__":
    unittest.main()
