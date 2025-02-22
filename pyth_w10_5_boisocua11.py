from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PYTH_W10_5
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

while True:
    n = input()
    if n == '-1':
        break
    
    xum = sum(int(n[i]) * (1 - 2 * (i % 2)) for i in range(len(n)))
    print("YES" if not xum % 11 else "NO")