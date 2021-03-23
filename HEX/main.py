from functools import reduce

cipher = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
bytearr = []

for index, letter in enumerate(cipher):
    if index % 2 == 0:
        bytearr.append(chr(int(letter + cipher[index + 1], 16)))

print(''.join(bytearr))