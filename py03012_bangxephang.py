from os import path
import sys, math

# PY03012
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
data = []
for _ in range(t):
    name = input()
    ac, submissions = mint()
    data.append((name, ac, submissions))

data = sorted(data, key = lambda x: (-x[1], x[2], x[0]))
for name, ac, submissions in data:
    print(name, ac, submissions)