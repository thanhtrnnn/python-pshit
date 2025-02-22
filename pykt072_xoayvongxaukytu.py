from os import path
import sys, math

# PYKT072
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

def stepcalc(des, src):
    if des == src: 
        return 0
    for i in range(len(des)):
        src = src[1:] + src[0]
        if src == des:
            return i + 1
    return -1

n = nint()
a = [input() for _ in range(n)]

ans = 10 ** 5
possible = True
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            pos = stepcalc(a[i], a[j])
            if pos == -1:
                possible = False
                break
            else: 
                cnt += pos
    ans = min(ans, cnt)

print(ans if possible else -1)