from os import path
import sys, math

# PYKT12026
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
    n, k = mint()
    a = aint()
    g = 0
    for i in range(1, n):
        g = math.gcd(g, a[i] - a[0])
    
    print('YES' if g and (k - a[0]) % g == 0 else 'NO')
