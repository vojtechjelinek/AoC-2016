from collections import Counter

with open("slepice.txt", "r") as f:
    message = f.read()

counters = [Counter() for _ in range(8)]
for line in message.splitlines():
    for i, char in enumerate(line):
        counters[i] += Counter(char)

deciphered = "".join(counter.most_common()[-1][0] for counter in counters)
print(deciphered)
