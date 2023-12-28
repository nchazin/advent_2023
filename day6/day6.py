import sys

from lib.tools import read_input

rows = read_input(sys.argv[1])


time = [int(x) for x in rows[0].split(':')[1].split(' ') if x.strip()!= '']
distance = [int(x) for x in rows[1].split(':')[1].split(' ') if x.strip()!= '']
big_time = int(rows[0].split(':')[1].replace(' ', ''))
big_distance = int(rows[1].split(':')[1].replace(' ', ''))

result = 1

for race in range(len(time)):
    print(f"race: {race}")
    r_time =  time[race]
    r_dis = distance[race]

    count = 0
    for i in range(1, r_time):
        move_distance = (r_time - i)*i
        if move_distance > r_dis:
            count +=1
    
    if count > 0:
        result *= count

print(result)

    #rtime - x)*x = r_dis
    #rtime *x - x**x = r_dis
    #rtime *x - x**x - r_dis = 0
    #rtime *x - rdis = x**2

count = 0
for i in range(1,big_time - 1):
    move_distance = (big_time - i)*i
    if move_distance > big_distance:
        count +=1

print(count)
