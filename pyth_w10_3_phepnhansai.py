from os import path
import sys, math

# PYTH_W10_3
input = lambda: sys.stdin.readline().rstrip("\r\n ")
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

# for line in sys.stdin:
#     s = line.strip()
#     if s == '-1':
#         break
while True:
    s = input()
    if s == '-1':
        break
    y, z = s.split()
    factor = sum(map(int, y))
    print(int(z) // factor)