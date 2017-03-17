from pprint import pprint
with open("slepice.txt", "r") as f:
    df = f.read()

nodes = []
for i, line in enumerate(df.splitlines()):
    nodes.append((i, int(line[23:27]), int(line[28:33]), int(line[35:40]), int(line.split("-")[2][1:4])))

i = 0
line = ""
map_ = ["" for _ in range(26)]
for node1 in nodes:
    viable_pairs = 0
    viable_pairs2 = 0
    for node2 in nodes:
        if node1 != node2 and node1[2] > 0 and node2[1] - node1[2] >= 0:
            viable_pairs += 1
        if node1 != node2 and node2[3] - node1[2] >= 0:
            viable_pairs2 += 1

    if viable_pairs2 > 1:
        map_[node1[4]] += '_'
    elif viable_pairs > 500:
        map_[node1[4]] += '.'
    else:
        map_[node1[4]] += '#'

pprint(map_)
