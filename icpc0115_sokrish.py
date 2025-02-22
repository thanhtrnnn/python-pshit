from os import path
from math import sqrt, gcd, ceil, floor
import sys

# ICPC0115 
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

factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880] 
t = nint()
for _ in range(t): 
    n = input() 
    s = 0 
    for digit in n: 
        s += factorial[int(digit)]
    
    print("Yes" if s == int(n) else "No")
