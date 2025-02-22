from os import path
from math import isqrt, gcd, ceil, floor
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

def condition(k):
    return True # Your condition here

t = nint()
for _ in range(t):
    n = nint()
    a = aint()

    lo = 0 # Set initial lower bound
    hi = 10 * 10 # Set initial upper bound
    eps = 1e-5      # Tolerance level

    while hi - lo > eps:
        mid = (lo + hi) / 2.0
        if (condition(mid)):
            lo = mid # or adjust hi based on your condition
        else:
            hi = mid

    answer = (lo + hi) / 2.0