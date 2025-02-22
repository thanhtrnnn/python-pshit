from os import path
import sys, math

# PYKT14023
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

n, q = mint()
a = [0] * (n + 2)
for _ in range(q):
    x, y = mint()
    a[x] += 1
    a[y + 1] -= 1

for i in range(1, n + 1):
    a[i] += a[i - 1]

print(*[a[i] % 2 for i in range(1, n + 1)])
    