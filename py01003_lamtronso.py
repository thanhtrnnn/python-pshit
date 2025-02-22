from os import path
from math import sqrt, gcd, ceil, floor
import re, sys

# PY01003
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(''.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

t = nint()
for _ in range(t):
    n = [int(c) for c in input()]

    for i in range(len(n) - 1, 0, -1):
        if n[i] >= 5:
            n[i - 1] += 1
        n[i] = 0
    
    printlist(n)