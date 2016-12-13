with open("slepice.txt", "r") as f:
    instructions = f.read()

valid = 0
lines = 0
for instruction in instructions.splitlines():
    triangle = sorted([int(instruction[i:i+5]) for i in range(0, 11, 5)])
    if triangle[0] + triangle[1] > triangle[2]:
        valid += 1

print(valid)
