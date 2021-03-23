def xor(a, b):
    formatted = '{:x}'.format(int(a, 16) ^ int(b, 16))

    return formatted.rjust(32, '0')

iv_start = "55cce30e8f5e0322f6da7e4f161b49c7"
with open('enc_file.txt', 'r') as rf:
    with open('dec_file.png', 'wb') as wf:
        block = rf.read(32)
        while block:
            result_block = xor(block, iv_start)
            wf.write(bytes.fromhex(result_block))

            block = rf.read(32)
