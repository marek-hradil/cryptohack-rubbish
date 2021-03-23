from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

'''
iv: bdd065af8985d4cfac54869903c22565
b1: 97e9a4ff2c72a3e3ac27d528f91814f0
b2: cc79923371972d9475691a46cba95e23

admin=False;expiry=1615316992
'''

cookie="admin=False;expiry=1615316992".encode()

padded = pad(cookie, 16)

print(padded)