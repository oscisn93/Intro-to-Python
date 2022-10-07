# 9.14
import string
from random import randint

class Lottery:
    
    def __init__(self,series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]):
        self.series = series
        self.numbers = [i for i in self.series if i in string.digits]
        self.letters = [c for c in self.series if c not in string.digits]
    def get_winning_ticket_number(self):
        n = 4
        winning_ticket = ''
        while (n!=0):
             winning_ticket += self.numbers[randint(0,(len(self.numbers)-1))]
             n -= 1
        n = 4
        while (n!=0):
             winning_ticket += self.letters[randint(0,(len(self.letters)-1))]
             n -= 1
        return winning_ticket
    
    def buy_ticket(self):
        return self.get_winning_ticket_number()

# lott = Lottery()
# winning_ticket_list = [lott.get_winning_ticket_number() for i in range(0,10)]

# for winning_ticket in winning_ticket_list:
#     print('Winning ticket:',winning_ticket)
