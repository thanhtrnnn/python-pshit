from os import path
import sys, math

# PY02052
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

n = nint()
a = [aint() for _ in range(n)]
k = nint()
upper, lower = 0, 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if j < i:
            lower += a[i][j]
        else:
            upper += a[i][j]

print('YES' if abs(upper - lower) <= k else 'NO')
print(abs(upper - lower))