from os import path
import sys, math

# PY01017
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
    i = 0
    while i < len(s):
        cnt = 1
        while i < len(s)-1 and s[i] == s[i + 1]:
            cnt += 1
            i += 1
        print(f'{cnt}{s[i]}', end = '')
        i += 1
    print()