from time import perf_counter as _p
from math import gcd

def letsgo():
    s = _p()
    res = 0
    for a in range(1, 6001):
        for b in range(a * 2 + 1, a * 3):
            if b > 12_000: break
            if gcd(a, b) == 1:
                res += 1

    print(res, _p() - s)


if __name__ == "__main__":
    letsgo()