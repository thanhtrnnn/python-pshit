from os import path
from math import sqrt, gcd
import sys

# PY1004
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

max = int(1e4 + 5)
isPrime = [True] * max

def sieve():
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(sqrt(max))):
        if isPrime[i]:
            for j in range(i * i, max, i):
                isPrime[j] = False
                
# def sieve():
#     for i in range(1, max):
#         minDivisor[i] = i
#     for i in range(2, int(math.sqrt(max))):
#         if minDivisor[i] == i:
#             for j in range(i * i, max, i):
#                 if minDivisor[j] == j:
#                     minDivisor[j] = i
# def isPrime(x):
#     if x < 2: 
#         return False
#     if x < 4: 
#         return True
#     if x % 2 == 0: 
#         return False
#     for i in range(3, int(sqrt(x)) + 1, 2):
#         if x % i == 0: 
#             return False
#     return True

t = nint()
sieve()
for _ in range(t):
    n = nint()
    res = 0
    for i in range(n):
        if gcd(i, n) == 1:
            res += 1
        
    # print('YES') if isPrime(res) else print('NO')
    print('YES' if isPrime[res] else 'NO')
    