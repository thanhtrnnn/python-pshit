from os import path
import sys, math

# PY01063
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
    s = input()
    n = input()
    print(s.count(n))
    # res = 0
    # start = 0
    # while start < len(s):
    #     a = []
    #     pos = s.find(n, start)
    #     if pos == -1:
    #         break
    #     res += 1
    #     start = pos + len(n)
    # print(res)
    