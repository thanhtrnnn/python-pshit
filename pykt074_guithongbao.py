from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PYKT074
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
notis = [input().strip() for _ in range(n)] # all the notifications
for s in notis:
    if len(s) < 100: 
        print(s) 
    else: 
        i = 100
        while s[i].isalpha(): 
            i -= 1 
        print(s[:i])