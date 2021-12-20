class WinChecker:
    """
    Checks through the rolled numbers from a game of Greed and gives the user
    a final score. TODO: improve this
    """

    def __init__(self, results):
        self.rolled_nums = results
        self.score = 0

    def get_score(self):
        return self.score

    def verify_wins(self):
        def triples(num):
            # used for triples
            if (num == 1):
                self.score += 1000
            else:
                self.score += num * 100
            
            self.rolled_nums[num] -= 3

        def singles(num):
            if (num != 1 and num != 5):
                pass
            elif (num == 1):
                self.score += 100
            elif (num == 5):
                self.score += 50
            
            self.rolled_nums[num] -= 1


        for num in self.rolled_nums:
            while self.rolled_nums[num] > 0:
                if (self.rolled_nums[num] >= 3):
                    triples(num)
                elif (self.rolled_nums[num] >= 1):
                    singles(num)
    
        print(f'You scored: {self.get_score()}')
