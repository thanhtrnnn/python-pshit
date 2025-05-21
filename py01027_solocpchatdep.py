from os import path
import sys, math

# PY01027
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
def isBeautiful(s):
    hit = 0
    for i in s:
        if i != '6' and i != '8': 
            return False
        if i == '8': 
            hit += 1
        else: 
            hit = 0
        if hit == 3: 
            return False
    return True

print('YES' if isBeautiful(input()) else 'NO')