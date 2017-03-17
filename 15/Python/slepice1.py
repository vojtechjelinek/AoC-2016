with open("slepice.txt", "r") as f:
    disc_infos = f.read()

discs = []
for info in disc_infos.splitlines():
    info = info.replace("Disc #", "").replace(" has ", ",").replace(".", "")
    info = info.replace(" positions; at time=0, it is at position ", ",")
    info = list(map(int, info.split(",")))
    discs.append({"wanted": (info[1]-info[0])%info[1],
                  "actual": info[2],
                  "max": info[1]})
discs.append({"wanted": (11-7)%11,
              "actual": 0,
              "max": 11})

max_pos = max(discs, key=lambda x: x["max"])
first_move = (max_pos["wanted"]-max_pos["actual"])%max_pos["max"]
for disc in discs:
    disc["actual"] = (disc["actual"] + first_move)%disc["max"]

step = max_pos["max"]
i = first_move
while True:
    i += step
    for disc in discs:
        disc["actual"] = (disc["actual"] + step)%disc["max"]
    for disc in discs:
        if disc["actual"] != disc["wanted"]:
            break
    else:
        print(i)
        break
