from os import path
import sys, math

# PY01034
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

def mind(s, i):
    pos = i
    for j in range(i + 1, len(s)):
        if s[j] < s[i]:
            if pos == i: 
                pos = j
            elif s[pos] < s[j]: 
                pos = j
    if s[pos] < s[i]: 
        return pos
    return -1

t = nint()
for _ in range(t):
    a = input()
    n, inv, min_d = len(a), -1, '0'
    for i in range(n - 2, -1, -1):
        if a[i] > a[i + 1]:
            inv = i
            break
    if inv == -1:
        print(-1)
        continue

    q = inv + 1 # find the smallest digit that is greater than a[inv] on the right
    for i in range(inv + 2, n):
        if a[i] > min_d and a[inv + 1] < a[i] < a[inv]:
            min_d = a[i]
            q = i
    a = a[:inv] + a[q] + a[inv + 1:q] + a[inv] + a[q + 1:]

    print(a if a[0] != '0' else -1)