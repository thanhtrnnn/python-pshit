from os import path
import sys, math

# PYKT087
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

mod = int(1e9 + 7) 
for _ in range(nint()): 
    n, k = mint()
    i = 0 
    res = 0 
    # divide & conquer
    while k: 
        if k & 1: # if k is odd
            res += pow(n, i, mod)
            res %= mod
        k >>= 1 
        i += 1 
    
    print(res)