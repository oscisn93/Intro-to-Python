# 9.14
import string
from random import randint
from typing import List


class Lottery:

    def __init__(self, series: List[str] = "0123456789ABCD".split('')):
        self.series = series
        self.numbers = [i for i in self.series if i in string.digits]
        self.letters = [c for c in self.series if c not in string.digits]

    def get_winning_ticket_number(self):
        n = 4
        winning_ticket = ''
        while n != 0:
            winning_ticket += self.numbers[randint(0, (len(self.numbers)-1))]
            n -= 1
        n = 4
        while n != 0:
            winning_ticket += self.letters[randint(0, (len(self.letters)-1))]
            n -= 1
        return winning_ticket

    def buy_ticket(self):
        return self.get_winning_ticket_number()


def get_win_attempts():
    lott = Lottery()
    winning_ticket_list = [lott.get_winning_ticket_number()
                           for i in range(0, 10)]
    print('The winning ticket list is: ', winning_ticket_list)

    count = 1
    won = False
    possible_winner = ''

    while not won:
        possible_winner = lott.buy_ticket()
        if possible_winner in winning_ticket_list:
            won = True
        count += 1

    print('Number of attempts to win:', count)
    print('Possible winner:', possible_winner)
