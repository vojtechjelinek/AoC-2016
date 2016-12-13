keypad1 = [["1", "2", "3"],
          ["4", "5", "6"],
          ["7" ,"8", "9"]]

keypad2 = [["x", "x", "1", "x", "x"],
          ["x", "2", "3", "4", "x"],
          ["5", "6", "7" ,"8", "9"],
          ["x", "A", "B", "C", "x"],
          ["x", "x", "D", "x", "x"]]

def find_code(code, keypad, pos):
    final_code = ""
    keypad = [["x"] + line + ["x"] for line in keypad]
    x_range = range(len(keypad[0]) + 2)
    keypad = [["x" for _ in x_range]] + keypad + [["x" for _ in x_range]]
    for line in code.splitlines():
        for char in line:
            if char == 'U':
                if keypad[pos[0] - 1][pos[1]] != "x":
                    pos[0] = pos[0] - 1
            elif char == 'D':
                if keypad[pos[0] + 1][pos[1]] != "x":
                    pos[0] = pos[0] + 1
            elif char == 'L':
                if keypad[pos[0]][pos[1] - 1] != "x":
                    pos[1] = pos[1] - 1
            elif char == 'R':
                if keypad[pos[0]][pos[1] + 1] != "x":
                    pos[1] = pos[1] + 1
        final_code += keypad[pos[0]][pos[1]]

    print(final_code)

with open("slepice.txt", "r") as f:
    code = f.read()

find_code(code, keypad1, [1, 1])
find_code(code, keypad2, [3, 1])
