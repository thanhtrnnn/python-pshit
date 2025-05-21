from os import path
import sys, math

# VI.01
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(float, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

xa, ya = mint()
xb, yb = mint()
xc, yc = mint()
ab = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
bc = math.sqrt((xb - xc) ** 2 + (yb - yc) ** 2)
ac = math.sqrt((xa - xc) ** 2 + (ya - yc) ** 2)

if ab + bc > ac and ab + ac > bc and bc + ac > ab:
    print('%.6f' % min(ab, bc, ac))