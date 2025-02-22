from bisect import bisect_left
from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY01011
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

nums = []

def isPalindrome(n):
    for i in n:
        if int(i) & 1:
            return False
    return n == n[::-1]

def add(start, end):
    for i in range(start, end, 22):
        if (isPalindrome(str(i))):
            nums.append(i)

add(22, 100)
add(2002, 8889)
add(200002, 888889)

t = nint()
for _ in range(t):
    n = nint()
    printlist(nums[:bisect_left(nums, n)])

# arr = []
# def Try(i,n,s):
#     if s!= "" and s[0]=='0': return
#     if i==n: return arr.append(int(s + ''.join(reversed(s))))
#     for j in range(0,9,2): Try(i+1,n,s + str(j))
# for i in range(1,5): Try(0,i,'')

# for t in range(int(input())):
#     n=int(input())
#     printlist(sorted(arr)[:bisect_left(arr,n)])