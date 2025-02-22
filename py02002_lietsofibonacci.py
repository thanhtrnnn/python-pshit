from os import path
from math import isqrt, gcd, ceil, floor
import sys, bisect

# PY02002
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

fibo = [1, 1]
for i in range(2, 100):
    fibo.append(fibo[i-1] + fibo[i-2])

t = nint()
for _ in range(t):
    a, b = mint()
    print(*fibo[a-1:b]) # ath fibo to bth fibo actually
