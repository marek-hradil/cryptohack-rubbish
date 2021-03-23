from Crypto.Cipher import AES
import hashlib
import random

def decrypt(ciphertext, word):
    hs = hashlib.md5(word.encode()).hexdigest()
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(hs)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return (None, None)

    return decrypted.hex()


searched = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'

with open('./words.txt') as f:
    words = [w.strip() for w in f.readlines()]


for word in words:
    decrypted = decrypt(searched, word)
    # is crypto
    if (decrypted and decrypted[:12] == '63727970746f'):
        print(decrypted)
