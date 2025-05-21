from os import path
import sys, math

# X.10
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

n, k = mint()
if k == 0:
    print(0)
    exit()
if k == 1:
    print(3)
    exit()
if n == 1:
    print(6 if k else 0)
    exit()

corners = 8 # 3 surfaces
edges = (n - 2) * 12 # 2 surfaces
faces = (n - 2) * (n - 2) * 6 # 1 surface
# print(corners, edges, faces)
res = min(corners, k) * 3 + max(0, min(edges, k - corners) * 2) + max(0, min(faces, k - corners - edges))
print(res)