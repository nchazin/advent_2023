from math import ceil
import sys
from dataclasses import dataclass


from lib.tools import read_input


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"Point {self.x}. {self.y}"


board = []
loop = {}

UP = ["|", "F", "7"]
DOWN = ["|", "L", "J"]
RIGHT = ["-", "J", "7"]
LEFT = ["-", "F", "L"]


def build_loop(node: Point, board, loop, match):
    if node in loop:
        return
    x = node.x
    y = node.y
    if y < 0 or y > len(board) or x <0 or x > len(board[0]):
        return
    pipe = board[y][x]
    if pipe not in match:
        return
    loop[node] = True
    try:
        if pipe == "|":
            build_loop(Point(x,y-1), board, loop, UP)
            build_loop(Point(x, y+1), board, loop, DOWN)
        elif pipe == "-":
            build_loop(Point(x-1,y), board, loop, LEFT)
            build_loop(Point(x+1, y), board, loop, RIGHT)
        elif pipe == "F":
            build_loop(Point(x+1,y), board, loop, RIGHT)
            build_loop(Point(x, y+1), board, loop, DOWN)
        elif pipe == "7":
            build_loop(Point(x-1,y), board, loop, LEFT)
            build_loop(Point(x, y+1), board, loop, DOWN)
        elif pipe == "J":
            build_loop(Point(x-1,y), board, loop, LEFT)
            build_loop(Point(x, y-1), board, loop, UP)
        elif pipe == "L":
            build_loop(Point(x+1,y), board, loop, RIGHT)
            build_loop(Point(x, y-1), board, loop, UP)
        elif pipe == "S":
            build_loop(Point(x,y-1), board, loop, UP)
            build_loop(Point(x, y+1), board, loop, DOWN)
            build_loop(Point(x-1,y), board, loop, LEFT)
            build_loop(Point(x+1, y), board, loop, RIGHT)
    except RecursionError:
        breakpoint()
        print(x,y)




def find_connected(x, y):
    if Point(x, y) in loop:
        return []
    loop[Point(x, y)] = True
    connected = []
    if board[y][x] == "|":
        if y - 1 >= 0:
            if board[y - 1][x] in ["|", "F", "7"]:
                if Point(x, y - 1) not in loop:
                    connected.append(Point(x, y - 1))
        if y + 1 < len(board):
            if board[y + 1][x] in ["|", "L", "J"]:
                if Point(x, y + 1) not in loop:
                    connected.append(Point(x, y + 1))
    elif board[y][x] == "-":
        if x - 1 >= 0:
            if board[y][x - 1] in ["-", "F", "L"]:
                if Point(x - 1, y) not in loop:
                    connected.append(Point(x - 1, y))
        if x + 1 < len(board[y]):
            if board[y][x + 1] in ["-", "J", "7"]:
                if Point(x + 1, y) not in loop:
                    connected.append(Point(x + 1, y))
    elif board[y][x] == "7":
        if x - 1 >= 0:
            if board[y][x - 1] in ["-", "F", "L"]:
                if Point(x - 1, y) not in loop:
                    connected.append(Point(x - 1, y))
        if y + 1 < len(board):
            if board[y + 1][x] in ["|", "L", "J"]:
                if Point(x, y + 1) not in loop:
                    connected.append(Point(x, y + 1))
    elif board[y][x] == "F":
        if x + 1 < len(board[y]):
            if board[y][x + 1] in ["-", "J", "7"]:
                if Point(x + 1, y) not in loop:
                    connected.append(Point(x + 1, y))
        if y + 1 < len(board):
            if board[y + 1][x] in ["|", "L", "J"]:
                if Point(x, y + 1) not in loop:
                    connected.append(Point(x, y + 1))
    elif board[y][x] == "J":
        if x - 1 >= 0:
            if board[y][x - 1] in ["-", "F", "L"]:
                if Point(x - 1, y) not in loop:
                    connected.append(Point(x - 1, y))
        if y + 1 < len(board):
            if board[y + 1][x] in ["|", "L", "J"]:
                if Point(x, y + 1) not in loop:
                    connected.append(Point(x, y + 1))
    elif board[y][x] == "L":
        if x + 1 < len(board[y]):
            if board[y][x + 1] in ["-", "J", "7"]:
                if Point(x + 1, y) not in loop:
                    connected.append(Point(x + 1, y))
        if y + 1 < len(board):
            if board[y + 1][x] in ["|", "L", "J"]:
                if Point(x, y + 1) not in loop:
                    connected.append(Point(x, y + 1))
    elif board[y][x] == "S":
        if y - 1 >= 0:
            if board[y - 1][x] in ["|", "F", "7"]:
                if Point(x, y - 1) not in loop:
                    connected.append(Point(x, y - 1))
        if y + 1 < len(board):
            if board[y + 1][x] in ["|", "L", "J"]:
                if Point(x, y + 1) not in loop:
                    connected.append(Point(x, y + 1))
        if x - 1 >= 0:
            if board[y][x - 1] in ["-", "F", "L"]:
                if Point(x - 1, y) not in loop:
                    connected.append(Point(x - 1, y))
        if x + 1 < len(board[y]):
            if board[y][x + 1] in ["-", "J", "7"]:
                if Point(x + 1, y) not in loop:
                    connected.append(Point(x + 1, y))
    return connected


if __name__ == "__main__":
    rows = read_input(sys.argv[1])
    #yikes
    sys.setrecursionlimit(20000)

    for y, row in enumerate(rows):
        row = row.strip()
        board.append(row)
        if (x := row.find("S")) != -1:
            startx = x
            starty = y

    build_loop(Point(startx, starty), board, loop, ['S'])
    print(ceil(len(loop)/2))
