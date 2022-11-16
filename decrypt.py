def L(N, lam, c):
    l = pow(c, int(lam), N ** 2)
    return int((l-1)/N)


def main(pri, c, N):
    lam = pri[0]
    u = pri[1]
    l = L(N, lam, c)

    m = pow(u * l, 1, N)
    return m
    # print(m)
