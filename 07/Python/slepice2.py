with open("slepice.txt", "r") as f:
    networks = f.read()

count = 0
for network in networks.splitlines():
    inside_brackets = False
    abas = set()
    babs = set()
    for i, char in enumerate(network[:-2]):
        if char in "[]":
            inside_brackets = not inside_brackets
        if char == network[i+2] and char != network[i+1] \
            and network[i+1] not in "[]":
            if inside_brackets:
                babs.add(network[i+1] + network[i] + network[i+1])
            else:
                abas.add(network[i:i+3])
    count += int(len(abas.intersection(babs)) > 0)
