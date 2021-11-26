from Crypto.Cipher import DES3

GOAL_BLOCK = '8245053c175cbc28'
ADD_BLOCK  = '0000000000000001'
KEY = '10000000000000000000000000000000'

cache = dict()

def xor(a, b):
    formatted = '{:x}'.format(int(a, 16) ^ int(b, 16)).rjust(len(a), '0')
    return formatted


def hex_perms(digits=16):
    x = 0
    max_ = 16 ** digits

    while x < max_:
        yield '{:0{len}x}'.format(x, len=digits)
        x += 1

gen = hex_perms()
cipher = DES3.new(bytes.fromhex(KEY), DES3.MODE_ECB)

for iv in gen:
    added = xor(iv, ADD_BLOCK)

    cached1 = cache.get(iv)
    cached2 = cache.get(added)

    c1 = cipher.encrypt(bytes.fromhex(iv)) if not cached1 else cached1
    c2 = cipher.encrypt(bytes.fromhex(added)) if not cached2 else cached2

    res = xor(c1.hex(), c2.hex())
    if res == GOAL_BLOCK:
        print('HOOORAY', iv)
        break

    if not cached1:
        cache[iv] = c1

    if not cached2:
        cache[added] = c2

    if len(cache) > 10000:
        cache = dict()
