from os import path
from math import sqrt, gcd, ceil, floor
import sys

# idhere
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

def is_prime(x):
    if x == 2: 
        return True
    if x < 2: 
        return False
    if x % 2 == 0: 
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0: 
            return False
    return True

def is_perfect_prime(n):
    rev_n = int(n[::-1])
    if not is_prime(int(n)): 
        return "No"
    if not is_prime(rev_n): 
        return "No"
    
    sum = 0
    for i in n:
        if not is_prime(int(i)):
            return "No"
        sum += int(i)
    if not is_prime(sum): 
        return "No"

    return "Yes"

t = nint()
for _ in range(t):
    n = input()
    print(is_perfect_prime(n))