from os import path
from math import sqrt, gcd, ceil, floor
import sys

# idhere
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

n, m = mint()
start = 0 if n > m else (1 if n < m else -1)
limit = start + (abs(n - m) - 1) * 2 
for i in range(n):
    a = input().split()
    if not start and i % 2 == 0 and i <= limit: 
        continue
    for j in range(m):
        if start == 1 and j % 2 and j <= limit: 
            continue
        print(a[j], end=' ')
    print()