PUZZLE_INPUT = 1352
INITIAL_POS = (1, 1)
WANTED_POS = (31, 39)

def is_wall(x, y):
    number = x*x + 3*x + 2*x*y + y + y*y + PUZZLE_INPUT
    n_of_ones = len(tuple(filter(lambda x: x == "1", bin(number))))%2
    return n_of_ones % 2 == 1

def get_accesible_poses(x, y):
    for mx, my in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        new_x, new_y = x + mx, y + my
        if new_x >= 0 and new_y >= 0 and not is_wall(new_x, new_y):
            yield (new_x, new_y)

def find_shortest_route():
    paths = [[INITIAL_POS]]
    while True:
        new_paths = []
        for path in paths:
            for next_pos in get_accesible_poses(*path[-1]):
                if next_pos == WANTED_POS:
                    return len(path)
                if next_pos not in path:
                    new_path = list(path)
                    new_path.append(next_pos)
                    new_paths.append(new_path)
        paths = list(new_paths)

print(find_shortest_route())
