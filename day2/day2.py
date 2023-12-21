import sys

with open(sys.argv[1]) as f:
    data = f.readlines()

startmap = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

# input looks like:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green


def create_map():
    return {"red": 0, "blue": 0, "green": 0}


sum = 0
for line in data:
    line = line.strip()
    id, stuff = line.split(":")
    id = id.split(" ")[1]
    failed = False
    for item in stuff.split(";"):
        item = item.strip()
        game = create_map()
        for part in item.split(','):
            part = part.strip()
            count, color = part.split(" ")
            count = int(count)
            game[color] += count
        print(game)
        print(startmap)
        for color in ["red", "blue", "green"]:
            if game[color] > startmap[color]:
                failed = True
                break
        if failed:
            break
    if not failed:
        sum += int(id)

print(sum)
