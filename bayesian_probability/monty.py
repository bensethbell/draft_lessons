import random

class Monty(object):
    def __init__(self):
        '''
        Initialize instance variables:
        doors: list of strings
        wins: integer
        total: integer
        '''
        self.doors = ['a', 'b', 'c']
        self.wins = 0
        self.total = 0

    def play(self, strategy):
        '''
        INPUT: function
        OUTPUT: Boolean
        Play the Monty Hall game once. The first choice is given by the
        argument chosen. Randomly choose a prize door and an empty door to
        reveal. The users strategy is given by the function strategy which
        takes a list of the door names, the prize door, and the door that was
        shown to be empty.
        Update the counters according to the results of the game and return
        True if the player wins, False otherwise.
        '''

        chosen = random.choice(self.doors)
        prize = random.choice(self.doors)
        empty = [x for x in self.doors if x not in [prize, chosen]][0]
        playermove = strategy(self.doors, chosen, empty)
        #print chosen, prize, empty, playermove
        if prize == playermove:
            self.wins += 1
            self.total += 1
            return True
        else:
            self.total += 1
            return False

    def play_n_times(self, n, strategy):
        '''
        INPUT: integer, function
        OUTPUT: None
        Play the Monty Hall game n times.
        '''
        for i in xrange(n):
            self.play(strategy)

        return "Wins: %d Total: %d Percentage: %f" % (self.wins, self.total, float(self.wins)/self.total)
