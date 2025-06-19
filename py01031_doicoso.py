from os import path
import sys, math

# idhere
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
    n, b = mint()
    # mxpow = 0
    # while b ** mxpow <= n:
    #     mxpow += 1
    # mxpow -= 1
    # res = []
    # for i in range(mxpow + 1):
    #     digit = n // (b ** mxpow)
    #     res.append(digit if digit < 10 else chr(ord('A') + digit - 10))
    #     n -= digit * (b ** mxpow)
    #     mxpow -= 1
    res = []
    while n:
        digit = n % b
        res.append(digit if digit < 10 else chr(ord('A') + digit - 10))
        n //= b

    print(*res[::-1], sep='')