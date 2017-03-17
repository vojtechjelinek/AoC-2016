data = "10010000000110000"
disk_size = 35651584

while len(data) < disk_size:
    data += "0" + "".join("0" if int(char) else "1" for char in data[::-1])
    print(len(data))
data = data[:disk_size]

while len(data)%2 == 0:
    checksum = ""
    for i in range(0, len(data), 2):
        if data[i] == data[i+1]:
            checksum += "1"
        else:
            checksum += "0"

    data = checksum

print(data)
