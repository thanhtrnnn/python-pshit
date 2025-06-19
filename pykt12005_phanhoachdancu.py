from os import path
import sys, math

# idhere
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
    n, c, d = mint()
    a = sorted(aint())

    max1, max2 = 0, 0
    if c > d: c, d = d, c
    x1, y1 = c, d

    while len(a):
        x = a.pop()
        if c:   
            max1 += x
            c -= 1
            continue
        if d:
            max2 += x
            d -= 1
            continue
        break
    
    max1 /= x1
    max2 /= y1

    print('%.6f' % (max1 + max2))