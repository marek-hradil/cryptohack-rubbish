import math

def is_same(p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]

def mod_inverse(a, p):
    return pow(a,p-2,p)

def add_points(p, q, curve, mod):
    if (is_same(p, (math.inf, math.inf))):
        return q

    if (is_same(q, (math.inf, math.inf))):
        return p
    
    if (p[0] == q[0] and p[1] == -q[1]):
        return (math.inf, math.inf)

    if (is_same(p, q)):
        lm = (3 * pow(p[0], 2) + curve[0]) * mod_inverse(2 * p[1], mod)
    else:
        lm = (q[1] - p[1]) * mod_inverse((q[0] - p[0]), mod)

    rx = (pow(lm, 2) - p[0] - q[0]) % mod
    ry = (lm * (p[0] - rx) - p[1]) % mod

    return (rx, ry)

P = (493, 5564)
Q = (1539, 4742)
R = (4403,5202)

C = (497, 1768)
MOD = 9739

print(add_points(add_points(add_points(P, P, C, MOD), Q,C,MOD), R, C, MOD))