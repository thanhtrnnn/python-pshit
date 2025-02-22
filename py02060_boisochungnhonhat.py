from os import path
import sys, math

# PY02060
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

maxn, mod = 10**6, 10**9 + 7
min_factor = [0] * (maxn + 1)
for i in range(2, int(math.isqrt(maxn))):
    if not min_factor[i]:
        min_factor[i] = i
        for j in range(i * i, maxn, i): 
            min_factor[j] = i

for i in range(math.isqrt(maxn), maxn + 1):
    if not min_factor[i]: 
        min_factor[i] = i

def legendre(p, n):
    """ Returns the power of prime p in N! using Legendre's formula. """
    count = 0
    while p <= n:
        count += n // p
        n //= p
    return count

def count(x, n):
    if n<x: return 0
    return n//x + count(x, n//x)

def binpow(n, k):
    if k == 1:
        return n
    res = binpow(n, k // 2)
    if k % 2:
        return res * res * n % mod
    else:
        return res * res % mod

t = nint()
for _ in range(t):
    a, b = mint()
    res = 1
    for i in range(2, b // 2 + 1):
        if min_factor[i] == i: # i is prime
            # calculate the power of prime i in (b choose a)
            res *= ((legendre(i, b) - legendre(i, a - 1)) * 2 + 1) % mod

    m = 0
    for i in range(b // 2 + 1, b + 1):
        if min_factor[i] == i: 
            m += 1
    res = res * binpow(3, m) % mod
    print(res)
