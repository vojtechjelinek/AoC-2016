TRAP_SITUATIONS = ("^^.", ".^^", "^..", "..^")
LINES_N = 400000

with open("slepice.txt", "r") as f:
    previous_line = "." + f.read().replace("\n", "") + "."

safe_tiles = sum(char == "." for char in previous_line) - 2
for i in range(LINES_N - 1):
    new_line = "."
    for j in range(1, len(previous_line)-1):
        new_line += "^" if previous_line[j-1:j+2] in TRAP_SITUATIONS else "."
    safe_tiles += sum(char == "." for char in new_line) - 1
    previous_line = new_line + "."

print(safe_tiles)
