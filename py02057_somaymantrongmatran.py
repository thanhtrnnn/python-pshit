from os import path
import sys, math

# PY02057
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

n, m = mint()
a = [aint() for _ in range(n)]
lucky = max(max(row) for row in a) - min(min(row) for row in a)

found = False
res = []
for i in range(n):
    for j in range(m):
        if a[i][j] == lucky:
            res.append((i, j))
            found = True

if not found:
    print('NOT FOUND')
else:
    print(lucky)
    for i, j in res:
        print(f'Vi tri [{i}][{j}]')
