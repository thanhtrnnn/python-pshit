from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY01069
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print('\n'.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

def Try(visited, s):
    if len(s) >= 4 and False not in visited and s[-1] != '2': 
        res.append(int(s))
    if len(s) == n: 
        return
    for i in range(4):
        branch_visited = visited.copy()
        branch_visited[i] = True
        Try(branch_visited, s + a[i])

n = nint()
a = ' '.join('2357').split()
res = []

Try([False] * 4, '')
printlist(sorted(res))