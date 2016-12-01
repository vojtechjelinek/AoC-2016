with open("wafu.txt", "r") as f:
    instructions = f.read()
pos = [0, 0]
poses = []
facing = 0
found = False
for instruction in instructions.split(", "):
    if instruction[0] == "R":
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4
    assert facing < 4

    if facing == 0:
        direction = 1
        value = 1
    elif facing == 1:
        direction = 0
        value = 1
    elif facing == 2:
        direction = 1
        value = -1
    elif facing == 3:
        direction = 0
        value = -1

    for i in range(0, int(instruction[1:])):
        pos[direction] = pos[direction] + value
        if tuple(pos) in poses and not found:
            found = True
            print("Distance of first intersection: " + str(abs(pos[0]-pos[1])))
        poses.append(tuple(pos))

print("Distance of end position: " + str(abs(pos[0]-pos[1])))
