from math import gcd
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

def lcm(a,b):
    return (a*b)//gcd(a,b)






def get_count(directions, curlabel, nodemap, destlist):
    count = 0
    for i in range(100000):
        for d in directions:
            if curlabel in destlist:
                break
            curnode = nodemap[curlabel]
            if d == 'L':
                curlabel = curnode.left
            elif d == 'R':
                curlabel = curnode.right
            count += 1
        if curlabel in destlist:
            break
    return  count

print(get_count(directions, curlabel, nodemap, ['ZZZ']))

start_labels = [key for key in nodemap.keys() if key[-1] == 'A']
#breakpoint()
end_labels = [key for key in nodemap.keys() if key[-1] == 'Z']

counts = []

for start_label in start_labels:
    counts.append(get_count(directions, start_label, nodemap, end_labels))

finds = counts

while len(finds) > 1:
    new_finds = list()
    new_finds = [lcm(finds[0], finds[1])] + finds[2:]
    finds = new_finds

print(finds[0])


