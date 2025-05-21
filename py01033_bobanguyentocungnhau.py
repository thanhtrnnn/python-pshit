from os import path
import sys, math

# PY01033
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

l, r = mint()
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        for k in range(j + 1, r + 1):
            if math.gcd(i, j) == math.gcd(j, k) == math.gcd(i, k) == 1:
                print(f'({i}, {j}, {k})')