from os import path
import sys, math

# PY02078
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(float, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

t = nint()
for _ in range(t):
    n = nint()
    a, b = [], []
    for _ in range(n):
        x, y = mint()
        a.append(x)
        b.append(y)

    dp = [1] * n
    res = 1
    for i in range(1, n):
        for j in range(i):
            # Check if (a[i], b[i]) can be appended to the increasing/ decreasing
            # subsequence ending with (a[j], b[j])
            if a[i] > a[j] and b[i] < b[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    
    print(res)