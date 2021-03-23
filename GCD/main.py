def gcd(a, b):
    r = a % b

    return b if r == 0 else gcd(b, r)

def extended_gcd(a, b):
    if a == 0:
        return (0, 1)

    x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1 
    y = x1 
    
    return x, y

print(extended_gcd(3, 13))