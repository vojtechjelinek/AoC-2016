def parse_instruction(instruction):
    if instruction[:3] == "cpy":
        value, name = instruction[4:].split(" ")
        return "{} = {}".format(name, value)
    elif instruction[:3] == "dec":
        name = instruction[4]
        return "{} -= 1".format(name)
    elif instruction[:3] == "inc":
        name = instruction[4]
        return "{} += 1".format(name)
    else:
        if_jump, distance = instruction[4:].split(" ")
        return "pos += {}-1 if {} else 0".format(distance, if_jump)

with open("slepice.txt", "r") as f:
    instructions = f.read()
a, b, c, d = 0, 0, 0, 0
pos = 0
instructions = list(map(parse_instruction, instructions.splitlines()))

while pos < len(instructions):
    exec(instructions[pos])
    pos += 1
print(a, b, c, d)
