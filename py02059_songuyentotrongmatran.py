from os import path
from math import isqrt, sqrt, gcd, ceil, floor
import sys

# PY02055, PY02059
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

def isPrime(x):
    if x == 2: 
        return True
    if x < 2:
        return False
    if x % 2 == 0: 
        return False
    for i in range(3, isqrt(x) + 1, 2):
        if x % i == 0: 
            return False
    return True

n, m = mint()
a = []
max_prime = 0
for i in range(n):
    a.append(aint())

max_pos = []
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            if max_prime == a[i][j]:
                max_pos.append((i, j))
            elif max_prime < a[i][j]:
                max_prime = a[i][j]
                max_pos = [(i, j)]

print(max_prime if max_pos else 'NOT FOUND')
for pos in max_pos:
    print(f'Vi tri [{pos[0]}][{pos[1]}]')
