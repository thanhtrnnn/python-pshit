from os import path
from math import isqrt, gcd, ceil, floor, log2
import sys

# PY02013
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

while n := nint():
    res = 1
    while n != 1:
        if n % 2:
            n = n * 3 + 1
        elif 2 ** int(log2(n)) == n:
            res += int(log2(n))
            break
        else:
            n //= 2
        # n = n * 3 + 1 if n % 2 else n // 2
        res += 1

    print(res)

