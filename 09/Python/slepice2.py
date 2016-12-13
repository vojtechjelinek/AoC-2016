def decompress(compressed, print_=False):
    decompressed = 0
    i = 0
    while i < len(compressed):
        if compressed[i] == "(":
            marker_end_pos = i + compressed[i:].find(")")
            marker = compressed[i+1:marker_end_pos]
            n, repeats = map(int, marker.split('x'))
            decompressed += decompress(compressed[marker_end_pos+1:marker_end_pos+n+1]) * repeats
            i = marker_end_pos + n + 1
        else:
            decompressed += 1
            i += 1
        if print_:

            print(i)
    return decompressed

with open("slepice.txt", "r") as f:
    compressed = f.read()

decompressed = decompress(compressed, True)
print(decompressed)
