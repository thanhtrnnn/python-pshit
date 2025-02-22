from os import path
from math import sqrt, gcd, ceil, floor
import sys

# ICPC0113
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

max = int(1e6)
isPrime = [True] * max

def sieve():
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(sqrt(max))):
        if isPrime[i]:
            for j in range(i * i, max, i):
                isPrime[j] = False

t = nint()
sieve()
for _ in range(t):
    n = input()
    existed = set()
    for i in range(13, int(n)):
        revn = int(str(i)[::-1])
        if isPrime[i] and isPrime[revn] and i < revn < int(n):
            print(i, revn, end = ' ')

    print()
    