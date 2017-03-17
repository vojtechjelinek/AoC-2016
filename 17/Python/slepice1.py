import hashlib

INITIAL_POS = (0, 0)
WANTED_POS = (3, 3)
PUZZLE_INPUT = "pvhmgsws"
SIDES = {0:'U', 1:'D', 2:'L', 3:'R'}

def is_open(path, side):
    hash_ = hashlib.md5((PUZZLE_INPUT + path).encode('utf-8')).hexdigest()
    return hash_[side] in "bcdef"

def get_accesible_poses(path, pos):
    for side, mx, my in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
        new_x, new_y = pos[0] + mx, pos[1] + my
        if 4 > new_x >= 0 and 4 > new_y >= 0 and is_open(path, side):
            yield (SIDES[side], (new_x, new_y))

def find_shortest_route():
    paths = [("", [INITIAL_POS])]
    while True:
        new_paths = []
        for path in paths:
            for next_pos in get_accesible_poses(path[0], path[-1][-1]):
                if next_pos[-1] == WANTED_POS:
                    print(len(path[0] + next_pos[0]))
                elif next_pos[-1] not in path:
                    new_path = list(path[-1])
                    new_path.append(next_pos[-1])
                    new_route = path[0] + next_pos[0]
                    new_paths.append((new_route, new_path))
        paths = list(new_paths)

print(find_shortest_route())
