from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY01002
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

exp = input().split()
# print('YES' if int(exp[-5]) + int(exp[-3]) == int(exp[-1]) else 'NO')
print('YES' if int(exp[0]) + int(exp[2]) == int(exp[-1]) else 'NO')