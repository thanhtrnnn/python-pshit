from os import path
from math import sqrt, gcd, ceil, floor, isqrt
import sys

# idhere
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

prime = [True] * (10**6 + 10) 
tri = [0] * (10**6 + 8) 
def sieve(): 
    prime[0] = prime[1] = False 
    for i in range(2, isqrt(10**6)): 
        if prime[i]: 
            for j in range(i * i, 10**6+1, i): 
                prime[j] = False

    for i in range(5, 10**6+1):
        if prime[i] and prime[i + 2] and prime[i + 6]:
            tri[i + 7] += 1
        if prime[i] and prime[i + 4] and prime[i + 6]: 
            tri[i + 7] += 1
        tri[i] += tri[i-1] 
                        
sieve()
for i in range(int(input())): 
    print(tri[int(input())])

