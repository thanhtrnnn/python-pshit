from os import path
import sys, math

# II.12
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

a0, b0, c0 = mint()
a1, b1, c1 = mint()
seconds = 0
if a0 > a1:
    a1 += 24
if b0 > b1:
    b1 += 60
    a1 -= 1
if c0 > c1:
    c1 += 60
    b1 -= 1

# wow so fast thanks
seconds = (a1 - a0) * 3600 + (b1 - b0) * 60 + (c1 - c0)
print(seconds)
