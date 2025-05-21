from os import path
import sys, math

# PY01013
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

def isPrime(x):
    if x == 2: 
        return True
    if x < 2: 
        return False
    if x % 2 == 0: 
        return False
    for i in range(3, math.isqrt(x) + 1, 2):
        if x % i == 0: 
            return False
    return True

t = nint()
for _ in range(t):
    a, b = mint()
    print('YES' if isPrime(sum(int(x) for x in str(math.gcd(a, b)))) else 'NO')