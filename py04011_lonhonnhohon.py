from collections import defaultdict
from os import path
import sys, math

# PY04011
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################
edges, names = [], set()
n = nint()

for i in range(n):
    a, sign, b = input().split()
    names.add(a)
    names.add(b)
    edges.append((a, b) if sign == '>' else (b, a))

adj = defaultdict(list)
for u, v in edges: 
    adj[u].append(v)

visited = defaultdict(int)
sys.setrecursionlimit(10**6)
def dfs(i):
    visited[i] = 1
    for j in adj[i]:
        if j not in visited: 
            if dfs(j): 
                return True
        if visited[j] == 1: 
            return True
    visited[i] = 2
    return False
    
containsCycle = False
for u in names:
    if u not in visited:
        if dfs(u):
            containsCycle = True
            break

print('impossible' if containsCycle else 'possible')
