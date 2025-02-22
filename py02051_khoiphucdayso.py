from os import path
from math import isqrt, gcd, ceil, floor
import sys

# PY02051
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
a = [] 
for i in range(n): 
    a.append(aint()) 
    
if n == 2: 
    print(a[0][1] // 2, a[0][1] // 2) 
else: 
    # a[i][j] = dp[i] + dp[j], i * j != 0
    dp = [0] * n
    dp[1] = (a[0][1] - a[0][2] + a[1][2]) // 2 # dp[0] + dp[1] - dp[0] - dp[2] + dp[1] + dp[2] = 2 * dp[1]
    dp[0] = a[0][1] - dp[1] 
    for i in range(2, n):
        dp[i] = a[0][i] - dp[0] 
    
    print(*dp)