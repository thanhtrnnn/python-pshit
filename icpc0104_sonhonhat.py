from os import path
from math import sqrt, gcd, ceil, floor
import re
import sys

# ICPC0104
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
    a = [int(x) for x in re.split("[a-z]+", input()) if x]
    res = min(a) if a else 0
    # s = input()
    # n = len(s)
    # res = int(1e6)
    # i = 0
    # while i < n:
    #     if '0' <= s[i] <= '9':
    #         curr = 0
    #         while i < n and '0' <= s[i] <= '9':
    #             curr = curr * 10 + int(s[i])
    #             i += 1
    #         res = min(res, curr)
    #     i += 1
    
    print(res)