from collections import defaultdict
from os import path
import sys, math

# PYKT2049
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
n = nint()

# Union-Find
parent = [-1] * (n + 1) # or list(range(n + 1))
def find(x):
    if parent[x] < 0: # or parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    parent[rootX] = rootY

def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y: 
        return
    if parent[y] < parent[x]: 
        x, y = y, x
    
    parent[x] += parent[y]
    parent[y] = x

for i in range(n):
    x, y, z = mint()
    if z == 1: 
        merge(x, y) # or union(x, y)
    else: 
        print(1 if find(x) == find(y) else 0)

# DFS (TLE)
# def dfs(u):
#     visited[u] = True
#     for v in adj[u]:
#         if not visited[v]: 
#             dfs(v)

# adj = defaultdict(list)
# for i in range(n):
#     u, v, op = mint()
#     if op == 1:
#         adj[u].append(v)
#         adj[v].append(u)
#     else:
#         visited = [False] * (n + 1)
#         dfs(u)
#         print(1 if visited[v] else 0)