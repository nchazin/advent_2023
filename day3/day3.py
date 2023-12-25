import sys
from pathlib import Path
#import regex as re
import re

with open(sys.argv[1]) as f:
    data = f.read()

rows = []
for row in data.split('\n'):
    if row != '':
        rows.append(row)


def check(rows, x, y, maxx, maxy):
    for xh in [-1,0,1]:
        for yh in [-1,0,1]:
            newx = x + xh
            newy = y + yh
            if newx < 0 or newx >= maxx or newy < 0 or newy >= maxy:
                continue
            c = rows[newy][newx]
            if c != '.' and not c.isdigit():
                return True
    return False

def is_part(rows, match, y, maxx, maxy):
    for x in range(match.start(), match.end()):
        if check(rows, x,y, maxx,maxy):
            return True
    return False   

sum = 0
            
maxy = len(rows) 
maxx = len(rows[0])

match_board = []
for _ in range(maxy):
    match_board.append([-1]*maxx)


def fill_board(board, y, match, maxx):
    for x in range(match.start(), match.end()):
        if x <= maxx:   
           board[y][x] = match


def gear_val(board, x, y, maxx, maxy):
    gear = 0
    matches = set()
    for xh in [-1,0,1]:
        for yh in [-1,0,1]:
            newx = x + xh
            newy = y + yh
            if newx < 0 or newx >= maxx or newy < 0 or newy >= maxy:
                continue
            if board[newy][newx] != -1:
                matches.add(board[newy][newx])
    matches = list(matches)
    if len(matches) == 2:
        gear = int(matches[0].group()) * int(matches[1].group()) 
    return gear

            


for y,row in enumerate(rows):
    for match in re.finditer('\d+', row):
        fill_board(match_board, y, match, maxx)
        val = int(match.group())
        if is_part(rows, match, y, maxx, maxy):
            sum += val
print(sum)


sum = 0
for y,row in enumerate(rows):
    for x, c in enumerate(row):
        if c == '*':
            val = gear_val(match_board, x,y, maxx, maxy)
            sum += val

print(sum)







