from os import path
import sys, math

# PYKT088
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
def solve(n):
    lim = math.isqrt(n)
    prime = [i for i in range(lim + 1)]
    for i in range(2, lim + 1):
        if prime[i] == i:
            for j in range(i * i, lim + 1, i):
                prime[j] = i

    cnt = 0
    for i in range(2, lim + 1):
        first, second = prime[i], prime[i // prime[i]]
        cnt += first * second == i and second != 1 and first != second
        cnt += prime[i] == i and i ** 8 <= n

    return cnt

print(solve(nint()))