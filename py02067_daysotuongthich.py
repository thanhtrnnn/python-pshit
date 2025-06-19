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
def validDivide(x, y):
    valid = False
    l, r = 1, x
    while abs(l - r) > 1:
        mid = (l + r) // 2
        if x // mid > y:
            l = mid
        elif x // mid < y:
            r = mid
        else:
            valid = True
            r = mid

    valid |= (x // r == y)
    return (valid, r)

n = nint()
a = aint()
mn = min(a)
for quotient in range(mn, 0, -1):
    res = 0
    for x in a:
        curr = validDivide(x, quotient)
        if not curr[0]:
            res = 0
            break
        res += curr[1]
    if res:
        print(res)
        break
