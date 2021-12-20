import random

class Dice:
    """
    Dice for the game of greed.
    """

    def __init__(self, num_of_die = 5):
        self.num_of_die = num_of_die   # default value set to 5 in case user does not want to pick different number
        self.rolled_nums = []
        self.totals = {}

    def __repr__(self) -> str:
        return str(self._num) 
    
    def set_num(self, num):
        """
        Adds to the list of rolls from a turn.
        """

        self.rolled_nums.append(num)

    def get_num(self):
        """
        Returns a list of the numbers rolled.
        """
        return self.rolled_nums

    def get_totals(self):
        """
        Returns a map of all the numbers rolled and how many times they occur.
        """
        return self.totals
    
    def roll_dice(self):
        """
        Plays a turn of Greed and rolls all die.
        """

        for i in range(self.num_of_die):
            cur_roll = random.randint(1, 6)
            self.set_num(cur_roll)
            print(f'Die # {i+1}: {cur_roll}')

        for num in self.rolled_nums:
            if num not in self.totals:
                self.totals[num] = 1
            else:
                self.totals[num] += 1
