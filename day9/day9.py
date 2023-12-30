import sys

from lib.tools import read_input

rows = read_input(sys.argv[1])

sum = 0
sum2 = 0
for row in rows:
    row = row.strip()
    numbers = list()
    numbers.append([int(n) for n in row.split(' ')])
        
    cur_num = numbers[0]   
    while(not all([ n == 0 for n in cur_num])):
        diffs = [cur_num[j+1] - cur_num[j] for j in range(len(cur_num) - 1)]
        numbers.append(diffs)
        cur_num = diffs

    numbers.reverse()
    for i, _ in enumerate(numbers):
        if i == 0:
            numbers[i].append(0)
        else:
            numbers[i].append(numbers[i][-1] + numbers[i-1][-1])
    sum += numbers[-1][-1]

    for i in range(1, len(numbers)):
        numbers[i].insert(0, (numbers[i][0] - numbers[i-1][0]))

    sum2 += numbers[-1][0]
    
print(sum)
print(sum2)

