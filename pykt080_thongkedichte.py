from os import path
import sys, math

# PYKT080
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

m, n = mint()
plot = [aint() for _ in range(m)]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
res = 0
visited = set()

for i in range(m):
    for j in range(n):
        if plot[i][j] == -1:
            for k in range(8):
                new_i, new_j = i + dx[k], j + dy[k]
                if ((new_i, new_j) not in visited 
                    and 0 <= new_i < m and 0 <= new_j < n): # and plot[new_i][new_j] != -1
                    visited.add((new_i, new_j))
                    res += plot[new_i][new_j]

print(res)