from pprint import pprint
from collections import deque
from itertools import combinations
FLOORS = ["first", "second", "third", "fourth"]

def parse_input(instructions):
    plan = [[] for _ in range(4)]
    floor = 0
    for instruct in instructions.splitlines():
        instruct = instruct.replace("The {} floor contains ".format(FLOORS[floor]), "")
        instruct = instruct.replace("and ", "").replace("a ", "").replace(", ", ",")
        instruct = instruct.replace("nothing relevant.", "").upper()
        if not instruct:
            continue
        for material, machine in map(lambda x: x.split() ,instruct.split(",")):
            plan[floor].append(material[0] + machine[0])
        floor += 1

    return plan

def valid_floor(floor):
    microchips = tuple(filter(lambda x: x[-1] == 'M' , floor))
    generators = tuple(map(lambda x: x[0] , filter(lambda x: x[-1] == 'G' , floor)))
    if not len(generators):
        return True
    for microchip in microchips:
        if microchip[0] not in generators:
            return False
    return True

def create_pairs(plan):
    materials = {}
    pairs = [[] for _ in range(5)]
    index = 0
    for floor in range(len(plan)):
        for machine in plan[floor]:
            if machine[0] not in materials:
                materials[machine[0]] = index
                index += 1
            pairs[materials[machine[0]]].append(floor)
    return tuple(tuple(pair) for pair in sorted(pairs))

def find_posible_routes(elevator, plan, visited):
    source_floor = plan[elevator]
    if elevator < 3:
        product_floor = plan[elevator + 1]
        for i in range(len(source_floor)):
            new_product_floor = product_floor + (source_floor[i],)
            new_source_floor = source_floor[:i] + source_floor[i+1:]
            if valid_floor(new_product_floor) and valid_floor(new_source_floor):
                new_plan = list(plan)
                new_plan[elevator] = new_source_floor
                new_plan[elevator + 1] = new_product_floor
                new_plan = tuple(new_plan)
                if create_pairs(new_plan) not in visited:
                    yield(elevator + 1, new_plan)
        for i, j in combinations(range(len(source_floor)), 2):
            new_product_floor = product_floor + (source_floor[i], source_floor[j])
            new_source_floor = source_floor[:min(i, j)] + source_floor[min(i, j)+1:]
            new_source_floor = new_source_floor[:max(i, j)-1] + new_source_floor[max(i, j):]
            if valid_floor(new_product_floor) and valid_floor(new_source_floor):
                new_plan = list(plan)
                new_plan[elevator] = new_source_floor
                new_plan[elevator + 1] = new_product_floor
                new_plan = tuple(new_plan)
                if create_pairs(new_plan) not in visited:
                    yield(elevator + 1, new_plan)
    if elevator > 0:
        product_floor = plan[elevator - 1]
        for i in range(len(source_floor)):
            new_product_floor = product_floor + (source_floor[i],)
            new_source_floor = source_floor[:i] + source_floor[i+1:]
            if valid_floor(new_product_floor) and valid_floor(new_source_floor):
                new_plan = list(plan)
                new_plan[elevator] = new_source_floor
                new_plan[elevator - 1] = new_product_floor
                new_plan = tuple(new_plan)
                if create_pairs(new_plan) not in visited:
                    yield(elevator - 1, new_plan)
        for i, j in combinations(range(len(source_floor)), 2):
            new_product_floor = product_floor + (source_floor[i], source_floor[j])
            new_source_floor = source_floor[:min(i, j)] + source_floor[min(i, j)+1:]
            new_source_floor = new_source_floor[:max(i, j)-1] + new_source_floor[max(i, j):]
            if valid_floor(new_product_floor) and valid_floor(new_source_floor):
                new_plan = list(plan)
                new_plan[elevator] = new_source_floor
                new_plan[elevator - 1] = new_product_floor
                new_plan = tuple(new_plan)
                if create_pairs(new_plan) not in visited:
                    yield(elevator - 1, new_plan)

def find_route(plan):
    n_machines = sum(len(floor) for floor in plan)
    routes = deque([(0, 0, tuple(tuple(floor) for floor in plan))])
    visited = set([(0, create_pairs(plan))])
    pprint(plan)
    return 0
    while routes:
        elevator, steps, plan = routes.popleft()
        for new_elevator, new_plan in find_posible_routes(elevator, plan, visited):
            if len(new_plan[-1]) == n_machines:
                return steps + 1
            else:
                routes.append((new_elevator, steps + 1, new_plan))
                visited.add((new_elevator, create_pairs(new_plan)))

with open("slepice.txt", "r") as f:
    instructions = f.read()

print(find_route(parse_input(instructions)))
