from os import path
import sys, math

# PY03014
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
    s = input()
    res = []
    st = []
    cnt = 0

    for c in s:
        if c == '(':
            cnt += 1
            st.append(cnt)
            res.append(cnt)
        elif c == ')':
            res.append(st.pop())

    print(*res)