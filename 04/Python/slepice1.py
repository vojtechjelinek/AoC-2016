import collections

with open("slepice.txt", "r") as f:
    rooms = f.read()

sum_ = 0
for instruction in rooms.splitlines():
    index = instruction.find("[")
    id_ = int(instruction[index-3:index])
    checksum = instruction[index+1:index+6]
    code = instruction[:index-3].replace("-", "")
    counter = collections.Counter(code)

    max_ = max(counter.values())
    same_occurence = ""
    for char in checksum:
        if max_ < counter[char]:
            break
        elif max_ == counter[char]:
            same_occurence += char
            del counter[char]
        elif max(counter.values()) != counter[char]:
            break
        else:
            if "".join(sorted(same_occurence)) != same_occurence:
                break
            same_occurence = char
            max_ = counter[char]
            del counter[char]
    else:
        if "".join(sorted(same_occurence)) == same_occurence:
            sum_ += id_

print(sum_)
