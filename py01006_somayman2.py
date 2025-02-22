from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY01006
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
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
    n = input()
    # key = n.count('4') + n.count('7')
    # print('YES' if key == len(n) else 'NO')
    for c in n:
        if c != '4' and c != '7':
            print('NO')
            break
    else:
        print('YES')