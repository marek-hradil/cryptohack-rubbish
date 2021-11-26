from Crypto.Cipher import DES3

KEY = '100000000000000000000000000000001000000000000000'

cipher = DES3.new(bytes.fromhex(KEY), DES3.MODE_ECB)
res = cipher.decrypt(bytes.fromhex('d0cd264b6f89d717'))

print(res.hex())