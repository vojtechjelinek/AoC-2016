with open("slepice.txt", "r") as f:
    instructions = f.read()
display = [[" " for _ in range(50)] for i in range(6)]
for instruction in instructions.splitlines():
    if instruction[:4] == "rect":
        width, height = (int(instr) for instr in instruction[5:].split("x"))
        display = [["█" if width > i else display[j][i] for i in range(50)] if height > j else display[j] for j in range(6)]
    elif instruction[7:10] == "row":
        pos, amount = instruction.split(" by ")
        pos, amount = int(pos.split("=")[1]), int(amount)
        for i in range(amount):
            val = display[pos].pop()
            display[pos].insert(0, val)
    else:
        pos, amount = instruction.split(" by ")
        pos, amount = int(pos.split("=")[1]), int(amount)
        column = [display[i][pos] for i in range(6)]
        for i in range(amount):
            val = column.pop()
            column.insert(0, val)
        display = [[column[j] if pos == i else display[j][i] for i in range(50)] for j in range(6)]
    
print("\n".join(["".join(line) for line in display]))
print(sum(("".join(line).count("█") for line in display)))
