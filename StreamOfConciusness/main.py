import requests
import random
import math

from Crypto.Cipher import AES
from Crypto.Util import Counter


def str_to_hex(s: str):
    return s.encode('utf-8').hex()

def make_req():
    res = requests.get(f'http://aes.cryptohack.org/stream_consciousness/encrypt/').json()
    text = res.get('ciphertext')

    print('--req--', len(text))
    return text

def xor(a, b):
    formatted = '{:x}'.format(int(a, 16) ^ int(b, 16)).rjust(len(a), '0')
    return formatted

def hex_to_ascii(h):
    try:
        d = bytearray.fromhex(h).decode()
        return d
    except:
        return '-'
'''
def get_all_ciphertexts():
    histogram = dict()
    for i in range(0, 100):
        length = str(make_req())
        if histogram.get(length):
            histogram[length] += 1
        else:
            histogram[length] = 1


    return histogram.keys()
ciphertexts = get_all_ciphertexts()

print("CIPHERTEXTS:")
for ciphertext in ciphertexts:
    print(ciphertext)
with open('./ciphertexts.txt', 'r') as f:
    ciphertexts = f.read().splitlines()

xores = []

for ciphertext1 in ciphertexts:
    num1, val1 = tuple(ciphertext1.split(' '))
    for ciphertext2 in ciphertexts:
        num2, val2 = tuple(ciphertext2.split(' '))

        if (val1 == val2):
            continue

        blockscount = math.ceil(max(len(val1), len(val2)) / 32)
        num = f'{num1}x{num2}'.ljust(6, '-')
        blocks = []

        for i in range(0, blockscount):
            block1 = val1[32 * i: 32 * (i + 1)]
            block2 = val2[32 * i: 32 * (i + 1)]
            block = xor(block1.ljust(32, '0'), block2.ljust(32, '0'))
            blocks.append(block)

        xores.append(num + '\t' + '\t'.join(blocks))
print("XORES:")
for xored in xores: 
    print(xored)
with open('./xores.txt', 'r') as f:
    xores = f.readlines()

modifieds = []
cribdrag = '63727970746f7b000000000000000000' # 14

for xored in xores:
    val = xored.split('\t')
    num = val[0]
    first_block = val[1]
    modified = xor(first_block, cribdrag)
    text = hex_to_ascii(modified)
    if (text):
        print(num, text[0:7])

print("MODIFIEDS")
for modified in modifieds:
    print(modified)


with open('./modifieds.txt', 'r') as f:
    modifieds = f.readlines()

texts = []
for modified in modifieds:
    try:
        d = bytearray.fromhex(modified).decode()
        texts.append(d)
    except:
        pass

for text in texts:
    print(text)
'''

def get_ciphertexts():
    ciphertexts = []
    with open('./ciphertexts.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            num, val = tuple(line.split(' '))
            ciphertexts.append(val)
    return ciphertexts

def cribdrag(keyivhex: str):
    ciphertexts = get_ciphertexts()

    max_len = 0
    for c in ciphertexts:
        if len(c) > max_len:
            max_len = len(c)

    ciphertexts_extended = [c.ljust(max_len, '0') for c in ciphertexts]
    ciphertexts_cut = [c[:len(keyivhex)] for c in ciphertexts_extended]
    plaintexts_hex = [xor(c, keyivhex) for c in ciphertexts_cut]
    plaintexts = [hex_to_ascii(p) for p in plaintexts_hex]

    print(str(len(keyivhex)) + 'of' + str(len('ef6123f01fa92733aec070bed885471fcbcbefdf13872a8e2035109a6dc853501bf2259125e5f48cd1603af9')))
    for i, p in enumerate(plaintexts):
        print(str(i + 1) + '\t' + p)

    return plaintexts

def is_printable_hex(h):
    return int(h, 16) in range(32, 127)


# cribdrag('a61503937ec700478ea2159eacea35')

cribdrag('a61503937ec700478ea2159eacea3571eba49aab3fa748fb541579ee4dab323e3b')