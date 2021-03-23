def split_to_nths(n, text):
    arr = []
    curr = ''
    for index, letter in enumerate(text):
        curr += letter
        if (index + 1) % n == 0:
            arr.append(curr)
            curr = ''

    return arr

encoding_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
ciphertext = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
bytesarr = split_to_nths(2, ciphertext)

print(bytesarr, [chr(int(b, 16)) for b in bytesarr])

bits = ''
for byte in bytesarr:
    bits += "{0:b}".format(int(byte, 16))

sextets = split_to_nths(6, bits)

output = ''
for sextet in sextets:
    index = int(sextet, 2)
    output += encoding_str[index]


print(output)