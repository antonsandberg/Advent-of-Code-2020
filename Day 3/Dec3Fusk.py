from math import prod

with open("Dec3Input.txt") as f:
    data = f.read().splitlines()

dx, dy = [0,0,0,0,0], [0,0,0,0,0]
slopes = [(1,1), (3,1), (5,1), (7,1),(1,2)]
trees = [0,0,0,0,0]

for line_number, line in enumerate(data):
    for char_index, slope in enumerate(slopes):
        if char_index == 4 and line_number % 2 != 0:
            continue
        posX = dx[char_index]
        posY = dy[char_index]
        if line[posX % len(line)] == "#":
            trees[char_index] += 1
        dx[char_index] += slope[0]
        dy[char_index] += slope[1]

print(prod(trees))
