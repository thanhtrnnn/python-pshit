from os import path
from math import sqrt, gcd, ceil, floor, log2
import sys

# ICPC0100
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
    n = nint()
    a = aint()
    res = 0

    for x, y in zip(a, a[1:]):
        be, lon = min(x, y), max(x, y)
        while (be := be << 1) < lon: # be := be * 2
            res += 1
        # if lon > 2 * be:
        #     res += int(log2((lon - 1) / be))

    print(res)