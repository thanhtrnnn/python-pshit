from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY02072
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

n, a = nint(), aint()
res = 0
m = max(a)
res, i = 0, 0
while i < n:
    if a[i] == m:
        curr = 0
        while i < n and a[i] == m:
            i += 1
            curr += 1
        res = max(res, curr)
    else: 
        i += 1

print(res)