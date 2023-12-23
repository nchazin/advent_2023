import sys
from pathlib import Path
#import regex as re
import re

with open(sys.argv[1]) as f:
    data = f.read()


rows = []
for row in data.split('\n'):
    rows.append(row)


def check(rows, x, y, maxx, maxy):
    for xh in [-1,0,1]:
        for yh in [-1,0,1]:
            newx = x + xh
            newy = y + yh
            if newx <= 0 or newx >= maxx or newy <= 0 or newy >= maxy:
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
            
maxy = len(rows) - 1
maxx = len(rows[0]) -1
for y,row in enumerate(rows):
    for match in re.finditer('\d+', row):
        val = int(match.group())
        if is_part(rows, match, y, maxx, maxy):
            sum += val
print(sum)
