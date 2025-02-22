from os import path
from math import sqrt, gcd, ceil, floor, log2
import sys

# ICPC0106
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

t = nint()
for _ in range(t):
    b = nint()
    s = input()
    res = ''
    if b == 2:
        res = s
    if b == 16:
        res = f'{int(s, 2):X}'
    if b == 8:
        res = f'{int(s, 2):o}'
    if b == 4:
        b = 2 # log2(b)
        while len(s) % b != 0:
            s = "0" + s
        i = 0
        while i < len(s):
            tmp = 0
            for j in range(i, i + b):
                tmp += int(s[j]) * (2 ** (b - j + i - 1))
            res += str(tmp) # if tmp < 10 else chr(ord('A') + tmp - 10)
            i += b
            
    print(res)
    
    
