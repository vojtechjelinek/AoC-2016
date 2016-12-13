with open("slepice.txt", "r") as f:
    compressed = f.read()

decompressed = ""
i = 0
while i < len(compressed):
    if compressed[i] == "(":
        marker_end_pos = i + compressed[i:].find(")")
        marker = compressed[i+1:marker_end_pos]
        n, repeats = map(int, marker.split('x'))
        decompressed += compressed[marker_end_pos+1:marker_end_pos+n+1] * repeats
        i = marker_end_pos + n + 1
    else:
        decompressed += compressed[i]
        i += 1

print(len(decompressed.replace("\n", "")))
