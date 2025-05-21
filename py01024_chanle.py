from os import path
import sys, math

# PY01024
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
    n = input()
    xum = sum(map(int, filter(str.isdigit, n))) # sum([int(c) for c in n if c.isdigit()])
    print("YES" if all(abs(int(n[i]) - int(n[i - 1])) == 2 for i in range(1, len(n))) and xum % 10 == 0 else "NO")