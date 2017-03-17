from pprint import pprint

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
    elif instruction[:3] == "tgl":
        distance = instruction[4:]
        return """
if pos+{0} < len(unparsed_instructions):
    if unparsed_instructions[pos+{0}][:3] == "inc":
        unparsed_instructions[pos+{0}] = "dec" + unparsed_instructions[pos+{0}][3:]
    elif unparsed_instructions[pos+{0}][:3] == "jnz":
        unparsed_instructions[pos+{0}] = "cpy" + unparsed_instructions[pos+{0}][3:]
    elif unparsed_instructions[pos+{0}][:3] == "dec":
        unparsed_instructions[pos+{0}] = "inc" + unparsed_instructions[pos+{0}][3:]
    elif unparsed_instructions[pos+{0}][:3] == "cpy":
        unparsed_instructions[pos+{0}] = "jnz" + unparsed_instructions[pos+{0}][3:]
    elif unparsed_instructions[pos+{0}][:3] == "tgl":
        unparsed_instructions[pos+{0}] = "inc" + unparsed_instructions[pos+{0}][3:]
instructions = list(map(parse_instruction, unparsed_instructions))
print(a, b, c, d)""".format(distance)
    else:
        if_jump, distance = instruction[4:].split(" ")
        return "pos += {}-1 if {} else 0".format(distance, if_jump)

with open("slepice.txt", "r") as f:
    unparsed_instructions = f.read().splitlines()

a, b, c, d = 9, 0, 0, 0
pos = 0
instructions = list(map(parse_instruction, unparsed_instructions))

while pos < len(instructions):
    exec(instructions[pos])
    pos += 1
print(a, b, c, d)
