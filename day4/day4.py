import sys
from lib.tools import read_input

rows = read_input(sys.argv[1])

cards = []

total = 0
for row in rows:
    wins =0
    p1, p2 = row.strip().split('|') 
    card = set([int(x) for x in  p2.split(' ') if x != ''])
    winners = [int(x) for x in p1.split(':')[1].split(' ') if x != '']
    for winner in winners:
        if winner in card:
            wins +=1
    total += int(2 ** (wins-1))


print(total)
