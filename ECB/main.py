from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

'''
# "00 00 00 00 00 00" + "xx xx" => "0208838cc799b38fdec36ea91e3bce08bf7cb5c61c342d50e3c308e1554f9946"

print(pad(bytes.fromhex("000000000000") + "1111111111".encode(), 16))

# print(len("0208838cc799b38fdec36ea91e3bce08bf7cb5c61c342d50e3c308e1554f9946"))

print(len("0208838cc799b38fdec36ea91e3bce08"))
print(len("bf7cb5c61c342d50e3c308e1554f9946"))

"cc cc cc cc cc cc cc cc cc 63 72 79 70 74 6f 7b"
"cc cc cc cc cc cc cc cc cc 63 72 79 70 74 6f 7b"
"xx xx xx xx xx xx xx xx xx xx xx xx xx xx xx xx"
"xx xx 7d"

"2723d2b2d437a76f191b7d8ea079978e"
"ebec2b6f8065cb9221f5380a5d22a1ee"
"5e2ce0b603bbc94beabb4d81280bd333
"6a5ca4f13e6ed2d5674f01f783113ced"

# --------------------------------------------------

"cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc 63"
"cc cc cc cc cc cc cc cc cc cc cc cc cc cc cc 63"
"xx xx xx xx xx xx xx xx xx xx xx xx xx xx xx xx"
"xx xx 7d"

"00000000000000000000000000000063000000000000000000000000000000"

"4efb28c43dfc878223ca3da8d186e0c0"
"4efb28c43dfc878223ca3da8d186e0c0"
"b4141fb4858ce57ec8a3f0aaf44d1bd4"
"fa3e47e6d7310bf1cbabe3b159c1beff"
# This means that first character of flag is c and proves concept

# -------------------------------------------------

# First word is crypto

"cc cc cc cc cc cc cc cc cc cc 63 72 79 70 74 6f"
"cc cc cc cc cc cc cc cc cc cc"
"xx xx xx xx xx xx xx xx xx xx xx xx xx xx xx xx"
"xx xx xx"

"0000000000000000000063727970746f00000000000000000000"

"ab75e6452752365129186852eb93f3ba"
"ab75e6452752365129186852eb93f3ba"
"2d158a0f6710538af642430d7fed2b8a"
"3f08a70f86500c6fefd593f3a8a979a5"

# -------------------------------------------------
# Challenge

"00 00 00 00 00 00 63 72 79 70 74 6f __ __ __ __"
"__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __"

# -------------------------------------------------

# Solution

"00 00 00 00 00 00 63 72 79 70 74 6f __ __ __ __"
"__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __"


"00 00 00 00 00 00 00 00 00 63 72 79 70 74 6f xx"
"00 00 00 00 00 00 00 00 00 63 72 79 70 74 6f"

# Encrypt with AES
# if first two blocks are the same, move to the next character

"00 00 00 00 00 00 63 72 79 70 74 6f 7b 70 33 6e"
"__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __"

"72 79 70 74 6f 7b 70 33 6e 36 75 31 6e 35 5f cc"
"00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 63"
"72 79 70 74 6f 7b 70 33 6e 36 75 31 6e 35 5f __"
"__ __ __ __ __ __ __ __ __"


'''


def encrypt(plaintext):
    return requests.get(f'http://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}').json().get('ciphertext')

def next_printable_char(prev_hex=None):
    if (prev_hex == None):
        return '20'
    elif (prev_hex == '7f'):
        return None
    else:
        new_val = int(prev_hex, 16) + 1
        return '{:02x}'.format(new_val)

def solve():
    padding_block = '00'
    known_parts = [['63', '72', '79', '70', '74', '6f', '7b', '70', '33', '6e', '36', '75', '31', '6e', '35', '5f']]
    known_blocks = ['68', '34', '37', '33', '5f', '33', '63', '62', '7d'] # crypto{p3n6u1n5_h4

    while(known_parts[-1][-1] != '7d'):
        new_char = next_printable_char()
        found = False
        while(not found):
            if (new_char == None):
                raise Exception('Smthing is wrong')
            padding_blocks = [padding_block for i in range(0, 15 - len(known_blocks))]
            blocks = known_parts[0][len(known_blocks) + 1:] + known_blocks + [new_char] + padding_blocks
            plaintext = ''.join(blocks)
            ciphertext = encrypt(plaintext)
            ciphertext_blocks = (ciphertext[0:31], ciphertext[64:95])
            if (ciphertext_blocks[0] == ciphertext_blocks[1]):
                found = True
                print('it was', new_char, len(ciphertext))
            else:
                print('it wasnt', new_char, len(ciphertext))
                new_char = next_printable_char(new_char)
        known_blocks += [new_char]

        if (len(known_blocks) == 16):
            known_parts += [''.join(known_blocks)]
        known_blocks = []

    print(known_blocks)
    print(known_parts)

solve()
