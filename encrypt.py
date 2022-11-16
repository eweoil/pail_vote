import random


def ran_r(N):
    return random.randrange(1, N)


def pro_c(N):
    r = ran_r(N)
    cr = pow(r, N, N ** 2)
    return cr


def main(pub,m):
    N = pub[0]
    g = pub[1]
    cg = pow(g, m, N ** 2)
    cr = pro_c(N)

    c = (cr*cg) % (N ** 2)
    return c


