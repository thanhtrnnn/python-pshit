from os import path
import sys, math

# VII.03
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

# bai nhu lon
n = nint() 
# for i in range(n):
#     for j in range(n - i, n):
#         print(j, end=' ')
#     for j in range(0, n - i):
#         print(j, end = ' ')
#     print()
res = [[j for j in range(n - i, n)] + [j for j in range(0, n - i)] for i in range(n)]
for row in res:
    print(*row)
