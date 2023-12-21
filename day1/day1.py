import sys
import regex as re

with open(sys.argv[1]) as f:
   data = f.readlines()

maps = {
"one" : '1',
"two" : '2',
"three" : '3',
"four" : '4',
"five" : '5',
"six" : '6' ,
"seven" : '7',
"eight" :'8' ,
"nine" : '9',
}

number_wang = r'\d|one|two|three|four|five|six|seven|eight|nine'

sum = 0
for line in data:
   ints = list()
   numbers = re.findall(number_wang, line,  overlapped=True)
   for number in numbers:
       ints.append(maps.get(number, number))
   val = ints[0] + ints[-1]
   print(val)
   sum += int(val)

print(sum)

       


   


