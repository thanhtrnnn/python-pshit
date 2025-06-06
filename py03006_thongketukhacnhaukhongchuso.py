from os import path
from math import sqrt, gcd, ceil, floor
import sys, re

# PY03006
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

t = nint()
words = {}
for _ in range(t):
    for token in re.split('[^a-z]', input().lower()):
        if token and token.isalpha():
            words[token] = words.get(token, 0) + 1

for x in sorted(words.items(), key=lambda x: (-x[1], x[0])):
    printlist(x)