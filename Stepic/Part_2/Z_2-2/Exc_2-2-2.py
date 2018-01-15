from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read().strip()

with open("passwords.txt", "rb") as inp_pass:
    passwords = inp_pass.read().splitlines()

for p in passwords:
    try:
        print('Check the ', p.decode('utf8'))
        print(decrypt(p.decode('utf8'), encrypted).decode('utf8'))
    except Exception:
        continue
    else:
        break
