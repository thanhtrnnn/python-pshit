from os import path
import sys, math

# PY01019
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
    n = len(s)

    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[n - i]) - ord(s[n - i - 1])):
            print("NO")
            break
    else:
        print("YES")