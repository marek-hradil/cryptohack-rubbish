import requests
import zlib

def get_all_variants(base, start=32, end=127):
    variants = []
    for val in range(start, end):
        variants.append(base + chr(val))

    return variants

def str_to_hex(s: str):
    return s.encode('utf-8').hex()

def make_req(s):
    res = requests.get(f'http://aes.cryptohack.org/ctrime/encrypt/{str_to_hex(s)}').json()
    print('-- req --', s[-1])
    text = res.get('ciphertext')

    return len(text)

def run():
    known_string = 'crypto{CRIME'
    while (known_string[-1] != '}'):
        shortest_variation = (None, None)
        for variant in get_all_variants(known_string):
            l = make_req(variant)
            if (not shortest_variation[0]) or (shortest_variation[1] > l):
                shortest_variation = (variant[-1], l)

        known_string += shortest_variation[0]
        print('-- FOUND --', known_string)
        shortest_variation = (None, None)

run()
