import hashlib


code = "uqwqemis"
salt = 0
password = ["#"] * 8
pass_length = 0
while True:
    m = hashlib.md5()
    m.update(code + str(salt))
    hash_ = m.hexdigest()
    if hash_[:5] == "00000":
        if hash_[5] in [str(i) for i in range(8)] and password[int(hash_[5])] == "#":
            print(hash_[:5])
            password[int(hash_[5])] = hash_[6]
            pass_length += 1
    if pass_length == 8:
        break
    salt += 1

print(password)
