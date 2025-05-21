from os import path
import sys, math

# PYKT037
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
    n, b = mint()
    i = int(math.log(n, b))

    for j in range(i + 1):
        d = n // (b ** i)
        print(d if d <= 9 else chr(ord('A') + d - 10), end='')
        n -= d * (b ** i)
        i -= 1
    print()