from collections import defaultdict

with open("slepice.txt", "r") as f:
    instructions = f.read().strip()

bots = defaultdict(list)
outputs = defaultdict(int)
instructions = instructions.splitlines()
unprocessed_instructions = []
while len(instructions):
    unprocessed_instructions = []
    for instruction in instructions:
        for bot_id in bots:
            if 17 in bots[bot_id] and 61 in bots[bot_id]:
                print(bot_id)
        if "value" in instruction:
            value, bot_id = instruction[6:].split(" goes to bot ")
            bots[bot_id].append(int(value))
        else:
            parsed_instruction = instruction[4:].replace(" gives low to ", ",").replace(" and high to ", ",").replace(" ", ",")
            bot_number, low_to, low_id, high_to, high_id = parsed_instruction.split(",")
            if len(bots[bot_number]) == 2:
                if low_to == "bot":
                    bots[low_id].append(min(bots[bot_number]))
                else:
                    outputs[low_id] = min(bots[bot_number])
                if high_to == "bot":
                    bots[high_id].append(max(bots[bot_number]))
                else:
                    outputs[high_id] = max(bots[bot_number])
                bots[bot_number] = []
            else:
                unprocessed_instructions.append(instruction)
    instructions = list(unprocessed_instructions)

print(outputs['0'] * outputs['1'] * outputs['2'])
