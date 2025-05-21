from os import path
import sys, math

# PYKT2078
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################
# dp[i][j] numbers has j 0 bits which has i + 1 bit (first bit = 1) -> i bits left contain j 0 bits
# or C(i, j) - binomial coefficient
dp = [[0] * 33 for _ in range(33)]
for i in range(33):
    dp[i][0] = 1
for i in range(1, 33):
    for j in range(1, 33):
        if i >= j:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

t = nint()
for _ in range(t):
    n, k = mint()
    if n == 0:
        print(1 if k == 1 else 0)
        continue

    s = bin(n)[2:]
    n = len(s)
    res, pre = 0, 0
    # count number of 0 bits in the first i bits
    for i in range(1, n):
        if s[i] == '1' and k > pre:
            res += dp[n - i - 1][k - pre - 1]
        if s[i] == '0':
            pre += 1
    
    # count number of 0 bits in the last bit
    # if pre == k, then the last bit is 1
    # if k == 1, then the first bit is 1
    res += sum(dp[i][k] for i in range(n - 1)) + (k == 1) + (pre == k)
    print(res)