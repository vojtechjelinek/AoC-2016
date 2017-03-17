import hashlib

code = b"uqwqemis"
salt = 0
password = ["#"] * 8
pass_length = 0
while pass_length < 8:
    hash_ = hashlib.md5(code + bytes(str(salt), 'utf-8')).hexdigest()
    if hash_[:5] == "00000":
        if hash_[5] in [str(i) for i in range(8)] and password[int(hash_[5])] == "#":
            password[int(hash_[5])] = hash_[6]
            pass_length += 1
            print(str(pass_length) + "/8 characters found")
    salt += 1

print("".join(password))
