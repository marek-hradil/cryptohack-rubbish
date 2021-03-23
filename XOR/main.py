def from_ascii(text):
    return [ord(letter) for letter in text]

def to_ascii(codes):
    return [chr(code) for code in codes]

def from_hex(text):
    bytearr = []
    for index, letter in enumerate(text):
        if index % 2 == 0:
            bytearr.append(int(letter + text[index + 1], 16))

    return bytearr

code = from_hex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
crypto = from_ascii("crypto{")
last_char = from_ascii("}")
key = from_ascii("myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymy")

print(len(key))

res = []
for hex_val, key_val in zip(code, key):
    res.append(hex_val ^ key_val)

print(''.join(to_ascii(res)))


# print(to_ascii(key), to_ascii([last_char[0] ^ code[-1]]))

'''
code = from_hex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(1, 256):
    shifted = [letter ^ i for letter in code]
    text = to_ascii(shifted)
    print(''.join(text))

key1 = to_ascii('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key1_key2 = to_ascii('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
key2_key3 = to_ascii('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
key1_key2_key3 = to_ascii('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = []
for code1, code2, code3, code4 in zip(key1, key1_key2, key2_key3, key1_key2_key3):
    key2 = code1 ^ code2
    key3 = code3 ^ key2
    flag.append(code4 ^ code1 ^ key2 ^ key3)


print(''.join(from_ascii(flag)))
'''

