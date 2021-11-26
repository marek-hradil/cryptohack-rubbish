from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import math
import hashlib

def is_same(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

def mod_inverse(a, p):
    return pow(a,p-2,p)

def add_points(p, q, curve, mod):
    if (is_same(p, (0, 0))):
        return q

    if (is_same(q, (0, 0))):
        return p
    
    if (p[0] == q[0] and p[1] == -q[1]):
        return (0, 0)

    if (is_same(p, q)):
        lm = (3 * pow(p[0], 2) + curve[0]) * mod_inverse(2 * p[1], mod)
    else:
        lm = (q[1] - p[1]) * mod_inverse((q[0] - p[0]), mod)

    rx = (pow(lm, 2) - p[0] - q[0]) % mod
    ry = (lm * (p[0] - rx) - p[1]) % mod

    return (rx, ry)

def multiply_point(point, n, curve, mod):
    q = (point[0], point[1])
    r = (0, 0)

    while n > 0:
        if n % 2 == 1:
            r = add_points(r, q, curve, mod)
        q = add_points(q, q, curve, mod)
        n = n // 2

    return r


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

def get_y(x: int) -> int:
    return (x^3 + 497*x + 1768) % 9739

def sq(a, p):
    return (a ^ int((p + 1) / 4)) % 9739


shared_secret = 0
iv = "cd9da9f1c60925922377ea952afc212c"
ciphertext = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"

print(get_y(4726), sq(get_y(4726), 9739))
