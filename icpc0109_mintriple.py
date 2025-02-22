from os import path
from math import sqrt, gcd, ceil, floor
import sys

# ICPC0109
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

import heapq, re

t = int(input())
for z in range(t):
    n = int(input())
    main = ' ' + input().replace(' ', '  ') + ' '
    i = -8
    ans = 0
    cnt = 0
    while i < 9 and cnt < 4:
        s = r'\d' * abs(i) + ' '
        if i < 0:
            s = '-' + s
        elif i > 0 :
            s = ' ' + s
        else :
            i += 1
            continue
        
        buf = heapq.nsmallest(3, re.findall(s, main))
        for x in buf:
            if cnt == 3:
                break
            ans += int(x)
            cnt += 1
        i += 1

    print(ans)