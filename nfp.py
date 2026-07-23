def diff(p, q):
    return p[0] - q[0], p[1] - q[1]


def cross(p, q):
    return p[0] * q[1] - q[0] * p[1]


def nfp(P, Q):
    m = len(P)
    n = len(Q)
    a = min(range(m), key=lambda i: P[i])
    b = max(range(n), key=lambda i: Q[i])
    R = []
    i = 0
    j = 0
    while i < m or j < n:
        R.append(diff(P[(a + i) % m], Q[(b + j) % n]))
        c = cross(diff(P[(a + i + 1) % m], P[(a + i) % m]), diff(Q[(b + j) % n], Q[(b + j + 1) % n]))
        if c >= 0 and i < m:
            i += 1
        if c <= 0 and j < n:
            j += 1
    return R
