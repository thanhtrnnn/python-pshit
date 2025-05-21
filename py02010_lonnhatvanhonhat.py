from os import path
import sys, math

# PY02010
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

while True:
    n = nint()
    if n == 0:
        break

    a = []
    minn, maxx = float('inf'), 0
    for i in range(n):
        a.append(nint())
        minn = min(minn, a[i])
        maxx = max(maxx, a[i])

    print(tostr((minn, maxx)) if minn != maxx else 'BANG NHAU')