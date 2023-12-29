import sys

from lib.tools import read_input

rows = read_input(sys.argv[1])

directions = rows[0].strip()

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

nodemap = {}

for row in rows[3:]:
    source, dest = row.strip().split('=')
    source = source.strip()
    dest = dest.replace('(', '').replace(')','').replace(' ','')
    left, right = dest.split(',')
    nodemap[source] = Node(left,right)

breakpoint()
print(nodemap)
    