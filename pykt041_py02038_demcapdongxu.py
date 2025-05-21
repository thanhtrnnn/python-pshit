from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PYKT041, PY02038
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

n = nint()
col = [0] * n
res = 0

for i in range(n):
    s = input()
    row_coins = 0
    for j in range(n):
        if s[j] == 'C':
            col[j] += 1
            row_coins += 1
    res += row_coins * (row_coins - 1) // 2

res += sum([x * (x - 1) // 2 for x in col])
print(res)