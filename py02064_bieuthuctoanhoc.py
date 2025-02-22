from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PY02064
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

def getFactor(index):
    if index % 5 == 0:
        return 5
    return index % 5 * pow(-1, index % 5 - 1)

t = nint()
for _ in range(t):
    n, k = mint()
    k *= 5
    a = [0] + aint()
    coef = [1, -2,  3, -4, 5]
    dp = [[0] * (n + 1) for _ in range(k + 1)] # dp[i][j] = max sum of i elems in first j elements

    for i in range(1, k + 1):
        # index = getFactor(i)
        index = coef[i % 5 - 1]
        dp[i][i] = index * a[i] + dp[i - 1][i - 1]
        for j in range(i + 1, n + 1):
            dp[i][j] = max(dp[i][j - 1], index * a[j] + dp[i - 1][j - 1])
    
    print(dp[k][n]) 