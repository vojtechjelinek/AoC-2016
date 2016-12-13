with open("slepice.txt", "r") as f:
    networks = f.read()

count = 0
for network in networks.splitlines():
    inside_brackets = False
    abba_outside = False
    abba_inside = False
    for i, char in enumerate(network[:-3]):
        if char in "[]" :
            inside_brackets = not inside_brackets
        if char == network[i+3] and network[i+1] == network[i+2] and \
            char != network[i+1]:
            if inside_brackets:
                abba_inside = True
            else:
                abba_outside = True

    count += int(not abba_inside and abba_outside)

print(count)
