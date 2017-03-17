from pprint import pprint
from itertools import permutations

with open("slepice.txt", "r") as f:
    MAP = f.read().splitlines()

def find_initial_pos():
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == "0":
                return (j, i)

def find_wanted_pos(number):
    number = str(number)
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] == number:
                return (j, i)

def is_wall(x, y):
    return MAP[y][x] == "#"

def get_accesible_poses(x, y):
    for mx, my in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        new_x, new_y = x + mx, y + my
        if 0 <= new_x < len(MAP[0]) and 0 <= new_y < len(MAP) and not is_wall(new_x, new_y):
            yield (new_x, new_y)

def find_shortest_route(initial_pos, wanted_pos):
    paths = [(0, initial_pos)]
    visited = set([initial_pos])
    while True:
        new_paths = []
        for path in paths:
            for next_pos in get_accesible_poses(*path[1]):
                if next_pos == wanted_pos:
                    return path[0] + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    new_paths.append((path[0] + 1, next_pos))
        paths = list(new_paths)

def solve():
    initial_pos = find_initial_pos()
    fwp = find_wanted_pos
    fsr = find_shortest_route
    distances = [[fsr(fwp(i), fwp(j)) if i != j else 0 for j in range(8)] for i in range(8)]
    min_distance = 1000000
    for path in permutations(range(1,8)):
        path = [0] + list(path)
        distance = 0
        for i in range(7):
            distance += distances[path[i]][path[i+1]]
        distance += distances[path[-1]][path[0]]
        min_distance = min(min_distance, distance)
    return min_distance

print(solve())
