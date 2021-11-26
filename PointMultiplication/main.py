def is_same(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

def mod_inverse(a, p):
    return pow(a,p-2,p)

def add_points(p, q, curve, mod):
    if (is_same(p, (0, 0))):
        return q

    if (is_same(q, (0, 0))):
        return p
    
    if (p[0] == q[0] and p[1] == -q[1]):
        return (0, 0)

    if (is_same(p, q)):
        lm = (3 * pow(p[0], 2) + curve[0]) * mod_inverse(2 * p[1], mod)
    else:
        lm = (q[1] - p[1]) * mod_inverse((q[0] - p[0]), mod)

    rx = (pow(lm, 2) - p[0] - q[0]) % mod
    ry = (lm * (p[0] - rx) - p[1]) % mod

    return (rx, ry)

def multiply_point(point, n, curve, mod):
    q = (point[0], point[1])
    r = (0, 0)

    while n > 0:
        if n % 2 == 1:
            r = add_points(r, q, curve, mod)
        q = add_points(q, q, curve, mod)
        n = n // 2

    return r

QA = (4726,)
n = 6534

C = (497, 1768)
MOD = 9739

print(multiply_point(QA, n, C, MOD))

