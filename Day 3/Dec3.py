import numpy as np

with open('Dec3Input.txt', 'r') as f:
    data = f.read().splitlines()
 # A
dx = 0
count = np.zeros(5)

for line in data:
    if line[dx % len(line)] == '#':
        count[0] += 1
    dx += 3

print(count[0])

# B
dx = 0


for line in data:
    if line[dx % len(line)] == '#':
        count[1] += 1
    dx += 1

print(count[1])

dx = 0


for line in data:
    if line[dx % len(line)] == '#':
        count[2] += 1
    dx += 5

print(count[2])

dx = 0

for line in data:
    if line[dx % len(line)] == '#':
        count[3] += 1
    dx += 7

print(count[3])

dx = 0

for i, line in enumerate(data):
    if ((i % 2) == 0) and (line[dx % len(line)] == '#'):
        count[4] += 1
    dx += 1

print(count[4])
print(count[0]*count[1]*count[2]*count[3]*count[4])
