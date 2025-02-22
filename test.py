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

N, mod = 10**6, 10**9+7
U = [0]*(N+1)
for i in range(2, int(sqrt(N))):
    if U[i]==0:
        U[i]=i
        for u in range(i, 1 + N//i): U[i*u]=i
for i in range(int(sqrt(N)), N+1):
    if U[i]==0: U[i]=i
def count(x, n):
    if n<x: return 0
    return n//x + count(x, n//x)
def pow(a, b):
    if b==0: return 1
    if b%2==1: return a*pow(a,b-1)%mod
    p = pow(a,b//2)
    return p*p%mod

for t in range(nint()):
    a, b = mint()
    ans = 1
    for i in range(2, b//2+1):
        if U[i]==i: ans = ans*((count(i, b) - count(i, a-1))*2+1)%mod
    m = 0
    for i in range(b//2+1, b+1):
        if U[i]==i: m+=1
    ans = ans*pow(3,m)%mod
    print(ans)

# input = sys.stdin.read
# data = input().splitlines()

# t = int(data[0])
# line_index = 1

# for z in range(t):
#     n = int(data[line_index])
#     arr = list(map(int, data[line_index + 1].split()))
#     x = y = z = 10 ** 8
#     for num in arr:
#         if num <= x:
#             z, y, x = y, x, num
#         elif num <= y:
#             z, y = y, num
#         elif num <= z:
#             z = num
            
#     print(x + y + z)
    
#     line_index += 2 


# import heapq, re

# t = int(input())
# for z in range(t):
#     n = int(input())
#     main = ' ' + input().replace(' ', '  ') + ' '
#     i = 8
#     ans = 0
#     cnt = 0
#     while i > -9 and cnt < 4:
#         s = r'\d' * abs(i) + ' '
#         if i < 0:
#             s = '-' + s
#         elif i > 0 :
#             s = ' ' + s
#         else :
#             i -= 1
#             continue

#         buf = heapq.nlargest(3, re.findall(s, main))
#         for x in buf:
#             if cnt == 3:
#                 break
#             ans += int(x)
#             cnt += 1
#         i -= 1

#     print(ans)