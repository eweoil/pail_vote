import prime
import math
import numpy


def produce(x):
    p = prime.generateLargePrime(x)
    q = prime.generateLargePrime(x)
    return p, q


def is_certain(p, q):
    t = math.gcd(p * q, (p - 1) * (q - 1))
    if p != q and t == 1:
        return True
    else:
        return False


def L(N, lam):
    g = N + 1
    l = pow(g, int(lam), N ** 2)
    return int((l-1)/N)


def main(x):
    t = produce(x)
    p = t[0]
    q = t[1]
    while is_certain(p, q) is not True:
        t = produce(x)
        p = t[0]
        q = t[1]

    N = p * q
    lam = numpy.lcm(p - 1, q - 1)
    kg = L(N, lam)
    u = pow(kg, -1, N)
    public = [N, N+1]
    private = [lam, u]
    # print(p, q)
    return public, private


# print(main(16))
