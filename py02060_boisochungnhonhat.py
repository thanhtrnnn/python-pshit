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
isPrime = [True] * (maxn + 1)
primes = []

for i in range(2, int(math.isqrt(maxn))):
    if isPrime[i]:
        for j in range(i * i, maxn, i): 
            isPrime[j] = False

for i in range(2, maxn + 1):
    if isPrime[i]: 
        primes.append(i)

def legendre(p, n):
    """ Returns the power of prime p in N! using Legendre's formula. """
    count = 0
    while p <= n:
        count += n // p
        n //= p
    return count

t = nint()
for _ in range(t):
    a, b = mint()
    res = 1 # ways to choose lcm(x, y) = P
    # P = a * (a + 1) * ... * b = b! / (a - 1)!
    for x in primes:
        if x > b:
            break
        count = legendre(x, b) - legendre(x, a - 1) # count of x in product([a, b])
        res = res * (2 * count + 1) % mod # ways to choose x^k, k = 0, 1, 2, ..., count

    print(res)
