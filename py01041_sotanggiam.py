from os import path
import sys, math

# PY01041
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
    n = input()
    i = 0
    while i < len(n) - 1 and n[i] < n[i + 1]: 
        i += 1
    while i < len(n) - 1 and n[i] > n[i + 1]: 
        i += 1
    
    print('YES' if i > 2 and i == len(n) - 1 else 'NO')