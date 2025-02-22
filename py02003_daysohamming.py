from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY02003
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

a = set()
max = int(1e18)
for i in range(60):
    n2 = 1 << i
    if n2 > max: 
        break
    for j in range(40):
        n3 = 3 ** j
        if n2 * n3 > max: 
            break
        for k in range(28):
            n5 = 5 ** k 
            if n2 * n3 * n5 > max:
                break
            a.add(n2 * n3 * n5)

nums = sorted(a)

def binary_search(l, r, v):
    if l > r: 
        return 'Not in sequence'
    mid = (l + r) // 2
    if nums[mid] == v: 
        return mid + 1
    if nums[mid] < v: 
        return binary_search(mid + 1, r, v)
    return binary_search(l, mid - 1, v)

for t in range(int(input())):
    print(binary_search(0, len(a), int(input())))