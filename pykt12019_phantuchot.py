from os import path
import sys, math

# PYKT12019
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

t = nint()
for _ in range(t):
    n = nint()
    a = aint()
    res = 0
    leftmax, rightmin = [0] * n, [0] * n
    leftmax[0] = a[0]
    rightmin[n - 1] = a[n - 1]

    for i in range(1, n):
        leftmax[i] = max(leftmax[i - 1], a[i])
        rightmin[n - i - 1] = min(rightmin[n - i], a[n - i - 1])

    for i in range(n):
        pivot = True
        if i and a[i] < leftmax[i - 1]:
            pivot = False
        if i < n - 1 and a[i] >= rightmin[i + 1]:
            pivot = False
        if pivot:
            res += 1

    print(res)