import sys

from lib.tools import read_input

rows = read_input(sys.argv[1])

directions = rows[0].strip()

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"L:{self.left} R:{self.right}"

nodemap = {}

for row in rows[2:]:
    source, dest = row.strip().split('=')
    source = source.strip()
    dest = dest.replace('(', '').replace(')','').replace(' ','')
    left, right = dest.split(',')
    nodemap[source] = Node(left,right)

    
curlabel = 'AAA'
count = 0


lastnode = set()

for i in range(100000):
    for d in directions:
        if curlabel == 'ZZZ':
            break
        curnode = nodemap[curlabel]
        if d == 'L':
            curlabel = curnode.left
        elif d == 'R':
            curlabel = curnode.right
        count += 1
    if curlabel == 'ZZZ':
        break

print(count)
