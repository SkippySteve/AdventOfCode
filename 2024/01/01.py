with open("input.txt") as f:
    lines = f.readlines()
    left = []
    right = []
    for line in lines:
        bothSides = line.split()
        left.append(bothSides[0])
        right.append(bothSides[1])

left.sort()
right.sort()
diff = 0
for i in range(len(left)):
    diff += int(max(left[i], right[i])) - int(min(left[i], right[i]))
print(diff)