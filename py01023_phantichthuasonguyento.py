from os import path
import sys, math

# PY01023
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
def primeFactors(n):
    out = ''
    for i in range(2, math.isqrt(n) + 1):
        if n % i:
            continue
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        out += f' * {i}^{cnt}'
        
    if n > 1: 
        out += f' * {n}^1'

    return out
    

t = nint()
for _ in range(t):
    n = nint()
    res = '1' + primeFactors(n)
    print(res)
    
