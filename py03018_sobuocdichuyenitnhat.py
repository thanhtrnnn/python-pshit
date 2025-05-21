import sys
from collections import deque

# PY03018
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
###############################################
# bai nhu lon 
a = [[]] * 1000 # avoid TLE
for t in range(nint()):
    n, m = mint()
    for i in range(n):
        a[i] = aint()
    
    q = deque([(0, 0)])
    res = [[0] * m for i in range(n)]
    while q:
        i, j = q.popleft()
        if i < n - 1:
            down = abs(a[i + 1][j] - a[i][j])
            if down and i + down < n and res[i + down][j] == 0:
                res[i + down][j] = res[i][j] + 1
                q.append((i + down, j))
        
        if j < m - 1:
            right = abs(a[i][j + 1] - a[i][j])
            if right and j + right < m and res[i][j + right] == 0:
                res[i][j + right] = res[i][j] + 1
                q.append((i, j + right))
        
        if i < n - 1 and j < m - 1:
            dr = abs(a[i + 1][j + 1] - a[i][j])
            if dr and i + dr < n and j + dr < m and res[i + dr][j + dr] == 0:
                res[i + dr][j + dr] = res[i][j] + 1
                q.append((i + dr, j + dr))

    print(res[n - 1][m - 1] if res[n - 1][m - 1] else -1)