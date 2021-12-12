import numpy as np

with open('Dec1Input.txt', 'r') as f:
    lines = f.readlines()
numbers = np.zeros(len(lines))
for i, line in enumerate(lines):
    numbers[i] = int(line.strip("'\'"))


def find2020(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[i]+numbers[j]+numbers[k] == 2020:
                    return numbers[i]*numbers[j]*numbers[k]


print(find2020(numbers))
