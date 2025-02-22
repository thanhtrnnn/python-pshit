from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PYTH_W10_4
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
    s = input().replace(' ', '')
    if s == '-1':
        break
    digits_sum = sum(map(int, s))
    last = 9 - digits_sum % 9 if digits_sum % 9 else 0
    print(str(int(s) + last))