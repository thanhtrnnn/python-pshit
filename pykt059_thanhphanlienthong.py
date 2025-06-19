from os import path
import sys, math

# PYKT059
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
def dfs(u, visited):
    for v in adj[u]:
        if v not in visited:
            visited.add(v)
            vertices.discard(v)
            dfs(v, visited)

n, m, x = mint()
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = mint()
    adj[u].append(v)
    adj[v].append(u)

vertices = set(range(1, n + 1))
dfs(x, set())
print(*vertices, sep='\n')