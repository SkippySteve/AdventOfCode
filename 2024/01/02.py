with open("input.txt") as f:
    lines = f.readlines()
    left = []
    right = []
    for line in lines:
        bothSides = line.split()
        left.append(bothSides[0])
        right.append(bothSides[1])

sum = 0
for num in left:
    prod = int(num) * right.count(num)
    sum += prod
print(sum)