import collections

with open("slepice.txt", "r") as f:
    instructions = f.read()

password = "abcdefgh"
password = collections.deque([char for char in password], len(password))
for instruction in instructions.splitlines()[:60]:
    operation, rest = instruction.split(" ", 1)
    if operation == "swap":
        op_type, rest = rest.split(" ", 1)
        if op_type == "position":
            x, y = map(int, rest.split(" with position "))
        else:
            letter_x, letter_y = rest.split(" with letter ")
            x, y = password.index(letter_x), password.index(letter_y)
        password[x], password[y] = password[y], password[x]
    elif operation == "rotate":
        op_type, rest = rest.split(" ", 1)
        if op_type == "based":
            letter = rest[-1]
            value = password.index(rest[-1])
            password.rotate(value + 2 if value >= 4 else value + 1)
        else:
            value = int(rest.split(" ")[0])
            password.rotate(value if op_type == "right" else -value)
    elif operation == "reverse":
        x, y = map(int, rest.replace("positions ", "").split(" through "))
        slice_to_reverse = list(password)[x:y+1]
        password.rotate(len(password)-y-1)
        for _ in range(len(slice_to_reverse)):
            password.pop()
        password.extend(reversed(slice_to_reverse))
        password.rotate(-(len(password)-y-1))
    elif operation == "move":
        x, y = map(int, rest.replace("position ", "").split(" to "))
        letter = password[x]
        del password[x]
        password.insert(y, letter)

print("".join(password))
