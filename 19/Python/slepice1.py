from math import log, floor

n_elves = 3014603

print((n_elves - 2 ** floor(log(n_elves, 2))) * 2 + 1)

magic_number = 3 ** floor(log(n_elves, 3))
if n_elves == magic_number:
    print(n_elves)
elif n_elves <= 2 * magic_number:
    print(n_elves - (3 ** floor(log(n_elves, 3))))
else:
    print(n_elves - (3 ** floor(log(n_elves, 3))) + (n_elves - 2 * magic_number))
