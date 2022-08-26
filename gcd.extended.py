from math import gcd

p = 26513
q = 32321

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

gcd, u, v = extended_gcd(p, q)

print(extended_gcd(p, q))
