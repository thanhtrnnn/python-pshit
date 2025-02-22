from os import path
from math import sqrt, gcd, ceil, floor
import sys

# ICPC0110
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

def solve():
    n = nint()
    a = aint()
    x, y, z = int(-1e8), int(-1e8), int(-1e8)
    i = 0
    while i < n:
        curr = a[i]
        if curr >= x:
            x, y, z = curr, x, y
        elif curr >= y:
            y, z = curr, y
        elif curr >= z:
            z = curr
        i += 1

    print(x + y + z)

t = nint()
for _ in range(t):
    solve()