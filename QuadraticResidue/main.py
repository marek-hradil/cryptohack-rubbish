def compute_roots(a, mod=29):
    roots = []
    for i in range(1, mod - 1):
        if (pow(i, 2) % mod == a):
            roots.append(i)

    return roots