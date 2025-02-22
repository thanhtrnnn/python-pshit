from os import path
from math import isqrt, sqrt, gcd, ceil, floor
import sys

# PY02059
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

def isPalindrome(x):
    return x >= 10 and str(x) == str(x)[::-1]

n, m = mint()
a = []
max_pali = 0
for i in range(n):
    a.append(aint())

max_pos = []
for i in range(n):
    for j in range(m):
        if isPalindrome(a[i][j]):
            if max_pali == a[i][j]:
                max_pos.append((i, j))
            elif max_pali < a[i][j]:
                max_pali = a[i][j]
                max_pos = [(i, j)]

print(max_pali if max_pos else 'NOT FOUND')
for pos in max_pos:
    print(f'Vi tri [{pos[0]}][{pos[1]}]')
