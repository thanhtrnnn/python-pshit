from os import path
from math import sqrt, gcd, ceil, floor
import sys

# ICPC0058
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

def dfs(start, end, curr, pot, visited):
    if curr == end:
        return False
    visited.add(curr)

    for i in adj[curr]:
        if i not in visited and i != pot:
            if not dfs(start, end, i, pot, visited):
                return False
    
    return True

def check(u, v, e): # check if there is a path from u to v without passing e
    q, un = [u], [0] * (n + 1)
    un[u] = 1
    while q:
        x = q.pop()
        if x == v: 
            return False # there is a path from u to v passing e
        for i in adj[x]:
            if un[i] == 0 and i != e: # i isnt e
                q.append(i)
                un[i] = 1
    return True

t = nint()
for _ in range(t):
    n, m, u, v = mint()
    adj = {x:[] for x in range(1, n + 1)}
    for i in range(m):
        a, b = mint()
        adj[a].append(b)

    res = 0
    for curr in range(1, n + 1):
        if curr != u and curr != v:
            if dfs(u, v, u, curr, set()): # if check(u, v, curr):
                res += 1 
    print(res)
    