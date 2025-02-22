from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PY02034
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

s = input()
freq = dict()
i = 0
while i + 1 < len(s):
    freq[s[i:i + 2]] = freq.get(s[i:i + 2], 0) + 1
    i += 2

for num in freq:
    print(num, freq[num])
