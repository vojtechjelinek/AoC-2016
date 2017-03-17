with open("slepice.txt", "r") as f:
    instructions = f.read()

valid = 0
lines = 0
triangles = [[0 for _ in range(3)] for _ in range(3)]
for instruction in instructions.splitlines():
    triangles[0][lines] = int(instruction[:5])
    triangles[1][lines] = int(instruction[5:10])
    triangles[2][lines] = int(instruction[10:])
    lines += 1
    if lines == 3:
        print(tuple(triangles[0]))
        print(tuple(triangles[1]))
        print(tuple(triangles[2]))
        for triangle in triangles:
            triangle = sorted(triangle)
            if triangle[0] + triangle[1] > triangle[2]:
                valid += 1
        lines = 0
        triangles = [[0 for _ in range(3)] for _ in range(3)]

print(valid)
