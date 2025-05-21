from os import path
import sys, math

# PY03015
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

def dfs(u):
    visited.add(u)
    for v in adj[u]:
        if v not in visited:
            dfs(v)

t = nint()
for _ in range(t):
    n, m = mint()
    adj = [[] for _ in range(n + 1)]
    visited = set()
    tplt = 0
    for _ in range(m):
        u, v = mint()
        adj[u].append(v)
        adj[v].append(u)

    # initial compute connected components
    for i in range(1, n + 1):
        if i not in visited:
            tplt += 1
            dfs(i)

    max_tplt, res = 0, 0
    for i in range(1, n + 1):
        curr = 0 # number of connected components after removing i
        visited = set([i])
        for j in range(1, n + 1):
            if j not in visited:
                curr += 1
                dfs(j)

        if curr > max_tplt:
            res = i
            max_tplt = curr

    print(res if max_tplt != tplt else 0)