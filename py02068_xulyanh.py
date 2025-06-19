from os import path
import sys, math

# PY02068
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

t = nint()
for _ in range(t):
    n, m, l = mint()
    a = [aint() for _ in range(n)]
    pre = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pre[i][j] += pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + a[i - 1][j - 1]

    # res = [[0] * (m - l + 1) for _ in range(n - l + 1)]
    for i in range(n - l + 1):
        for j in range(m - l + 1):
            x = pre[l + i][l + j] - pre[i][l + j] - pre[l + i][j] + pre[i][j]
            x //= (l * l)
            print(x, end=' ')
        print()

    # print(*[tostr(line) for line in res], sep='\n')