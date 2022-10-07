from Lottery import Lottery

lott = Lottery()
winning_ticket_list = [lott.get_winning_ticket_number() for i in range(0,10)]
print('The winning ticket list is: ', winning_ticket_list)

count = 1
won = False
possible_winner = ''

while not won:
    possible_winner = lott.buy_ticket()
    if possible_winner in winning_ticket_list:
        won = True
    count += 1
    
print('Number of attempts to win:',count)
print('Possible winner:', possible_winner)