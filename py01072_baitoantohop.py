from itertools import combinations
from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PY01072
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

# def backtrack(i, pos):
#     if i == k:
#         printlist(ans)
#         return
    
#     for j in range(pos, len(res)):
#         ans[i] = res[j]
#         backtrack(i + 1, j + 1)

n, k = mint()
comb = combinations(sorted(set(input().split()), key = int), k)
print('\n'.join([' '.join(x) for x in comb]))
# res = sorted(set(aint()))
# ans = [0] * k
# backtrack(0, 0)
