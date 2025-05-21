from os import path
import sys, math

# PYKT078
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

t = nint()
for _ in range(t):
    n, m = mint()
    a = aint()
    neg, pos = [], []
    maxi = 0

    for i in range(n):
        x = a[i]
        if x < 0:
            neg.append(x)
        else:
            pos.append(x)

    for i in range(len(pos)):
        if pos[i] > pos[maxi]:
            maxi = i
    pos.insert(maxi, m)
    
    print(tostr(neg + pos))