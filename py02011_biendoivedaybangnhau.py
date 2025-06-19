from os import path
import sys, math

# PY02011
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

n = nint()  
a = aint()
minsteps, pos = 1e7, 0
for i in range(n):
    curr = sum(abs(a[j] - a[i]) for j in range(n))
    if curr < minsteps:
        minsteps = curr
        pos = i

print(minsteps, a[pos])