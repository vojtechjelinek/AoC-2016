with open("slepice.txt", "r") as f:
    ranges = [tuple(map(int, range_.split("-"))) for range_ in f.read().splitlines()]
    ranges = sorted(ranges, key=lambda x: x[0])

i = 0
prev_min = prev_max = 0
merged_ranges = []
for min_, max_ in ranges:
    if min_ - 1 > prev_max:
        merged_ranges.append((prev_min, prev_max))
        prev_min = min_
    prev_max = max(prev_max, max_)

print(merged_ranges[0][1] + 1)
print(len(merged_ranges))
