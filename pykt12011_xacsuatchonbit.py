from os import path
import sys, math

# PYKT12011
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
    n, k = mint()
    s = input()
    a = [0] * (n + 1)
    cases = 0
    for i in range(1, n + 1):
        a[i] = a[i - 1] + (s[i - 1] == '1')
    
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            cases += 2 * (a[i] - 1) + 1 if i <= k else 2 * (a[i] - a[i - k - 1] - 1) + 1

    x = math.gcd(cases, n * n)
    print('0/1' if cases == 0 else f'{cases // x}/{n * n // x}')