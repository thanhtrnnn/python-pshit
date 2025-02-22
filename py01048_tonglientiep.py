from os import path
from math import sqrt, gcd, ceil, floor, isqrt
import sys

# PY01048
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

t = nint()
for _ in range(t):
    n = 2 * nint()
    res = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: # i is a divisor of n
            a, b = n // i, i # a * b = n
            k = a - b + 1 
            if k % 2 == 0: 
                l = (a - b + 1) // 2
                r = a - l 
                if r and r > l:
                    res += 1

    #A sum of k consecutive integers starting at x is:

    # x + (x + 1) + (x + 2) + … + (x + k - 1)

    # The sum is kx + k(k - 1)/2.

    # Setting that equal to n and solving for x gives:

    # kx + k(k - 1)/2 = n ⇒ 2n = k(2x + k - 1).

    # If 2n = a · b, one can interpret a = (2x + k - 1) and b = k. Solving for x yields:

    # x = (a - (k - 1)) / 2 = (a - b + 1) / 2.

    # We need x > 0 (i.e. a - b + 1 > 0, or equivalently a > b - 1), and (a - b + 1) must be even so that x is an integer.

    # The code iterates over all divisors i = b of n (and a = n // b) to find suitable pairs (a, b). It checks these conditions and counts valid solutions.
    # n = nint()
    # res = 0
    # for i in range(1, 42722):
    #     if n <= i * (i + 1) // 2:
    #         break
    #     if (n - i * (i + 1) // 2) % (i + 1) == 0: 
    #         res += 1
    print(res)
