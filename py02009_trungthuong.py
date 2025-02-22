from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PY02009
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
    freq = {}
    for i in range(n):
        x = nint()
        freq[x] = freq.get(x, 0) + 1
    freq = sorted(freq.items(), key = lambda x: (-x[1], x[0]))
    print(freq[0][0])