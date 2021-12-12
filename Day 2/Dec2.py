
with open('Dec2Input.txt', 'r') as f:
    lines = f.readlines()

# A
count = 0
for line in lines:
    line = line.split(" ")
    min, max = line[0].split('-')
    letter = line[1].strip(':')
    password = line[2].strip('\n')
    if (password.count(letter) >= int(min)) and (password.count(letter) <= int(max)):
        count += 1

print(count)

# B
count = 0
for line in lines:
    line = line.split(" ")
    i1, i2 = line[0].split('-')
    letter = line[1].strip(':')
    password = line[2].strip('\n')
    if (password[int(i1)-1] == letter) and (password[int(i2)-1] != letter):
        count += 1
    elif (password[int(i1)-1] != letter) and (password[int(i2)-1] == letter):
        count += 1
print(count)
