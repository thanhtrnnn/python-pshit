from os import path
import sys, math

# PY02017
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
# for _ in range(nint()): _ = nint(); print(__import__('functools').reduce(lambda a, b: a ^ b, mint(), 0))
t = nint()
for _ in range(t):
    n = nint()
    res = 0
    for x in aint():
        res ^= x
    print(res)