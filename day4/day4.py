import sys
from lib.tools import read_input

rows = read_input(sys.argv[1])

cards = []
counts = [1]*len(rows)

total = 0
for row in rows:
    wins =0
    p1, p2 = row.strip().split('|') 
    card = set([int(x) for x in  p2.split(' ') if x != ''])
    winners = [int(x) for x in p1.split(':')[1].split(' ') if x != '']
    for winner in winners:
        if winner in card:
            wins +=1
    cards.append(wins)

total = 0
for cn, card in enumerate(cards):
    if card > 0:
        for cn_p in range(cn+1, cn++1+card):
            counts[cn_p] += 1*counts[cn]
        total += 2**(card-1)

print(total)
print(sum(counts))
