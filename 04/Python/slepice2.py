with open("slepice.txt", "r") as f:
    rooms = f.read()

sum_ = 0
for instruction in rooms.splitlines():
    index = instruction.find("[")
    id_ = int(instruction[index-3:index])
    checksum = instruction[index+1:index+6]
    code = instruction[:index-3].replace("-", "")

    new_code = ""
    for char in code:
        new_code += chr((ord(char) - 97 + id_) % 26 + 97)
    code = new_code
    if "north" in code:
        print(id_)
