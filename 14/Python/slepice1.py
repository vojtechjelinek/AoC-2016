import hashlib

code = "jlmsuwbz"
salt = 0
password = ["#"] * 8
pass_length = 0
triplets = []
n_keys = 0
while True:
    hash_ = hashlib.md5((code + str(salt)).encode('utf-8')).hexdigest()
    for _ in range(2016):
        hash_ = hashlib.md5(hash_.encode('utf-8')).hexdigest()

    fiftets = []
    new_triplets = []
    for i in range(len(hash_)-4):
        if hash_[i] == hash_[i+1] == hash_[i+2] == hash_[i+3] == hash_[i+4]:
            fiftets.append(hash_[i])
    for index, letter in triplets:
        if salt <= index + 1000:
            if letter in fiftets:
                n_keys += 1
                if n_keys == 64:
                    print(index)
            else:
                new_triplets.append((index, letter))

    triplets = list(new_triplets)
    for i in range(len(hash_)-2):
        if hash_[i] == hash_[i+1] == hash_[i+2]:
            triplets.append((salt, hash_[i]))
            break
    salt += 1
