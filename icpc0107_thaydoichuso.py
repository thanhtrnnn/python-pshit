from os import path
from math import sqrt, gcd, ceil, floor
import sys

# ICPC0107
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
sint = lambda: map(str, input().split())
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

def convert(a, b, p, q): 
    a = a.replace(p, q) 
    b = b.replace(p, q) 
    return int(a) + int(b) 

t = nint()
for _ in range(t):
    p, q = sint()
    buf = input().split()
    # a, b maybe same line
    a = buf[0]
    b = buf[1] if len(buf) > 1 else input() 

    x = convert(a, b, p, q) 
    y = convert(a, b, q, p) 
    print(min(x, y), max(x, y)) 