import binascii
def from_hex(text):
    bytearr = []
    for index, letter in enumerate(text):
        if index % 2 == 0:
            bytearr.append(int(letter + text[index + 1], 16))

    return bytearr

with open('../assets/flag.png', 'rb') as flagFile:
    flagContent = from_hex(binascii.hexlify(flagFile.read()))

with open('../assets/lemur.png', 'rb') as lemurFile:
    lemurContent = from_hex(binascii.hexlify(lemurFile.read()))

key = ''
for index, item in enumerate(flagContent[:3000]):
    key += chr(item ^ lemurContent[index])

print(key)
