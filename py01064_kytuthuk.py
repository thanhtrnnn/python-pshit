from os import path
import sys, math

# PY01064
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

def find(n, k):
    if n == 1:
        return 'A'
    half = 2 ** (n - 1)
    if k == half:
        return chr(ord('A') + n - 1)
    elif k < half:
        return find(n - 1, k)
    else:
        return find(n - 1, k - half)

t = nint()
for _ in range(t):
    n, k = mint()
    print(find(n, k))