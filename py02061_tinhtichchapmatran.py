from os import path
import sys, math

# PY02061
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

def solve():
    for i in range(n - 2):
        for j in range(m - 2):
            for x in range(3):
                for y in range(3):
                    res[i][j] += ker[x][y] * a[i + x][j + y]

    return sum(sum(row) for row in res)

t = nint()
for _ in range(t):
    n, m = mint()
    a = [aint() for _ in range(n)]
    ker = [aint() for _ in range(3)]
    res = [[0] * (m - 2) for _ in range(n - 2)]

    # for i in range(n - 2):
    #     col_st, col_en = i, i + 3 
    #     for j in range(m - 2):
    #         row_st, row_end = j, j + 3 
    #         a_slice = [row[row_st:row_end] for row in a[col_st:col_en]] 
    #         res[i][j] = sum(a_slice[x][y] * ker[x][y] for x in range(3) for y in range(3))

    # print(sum(sum(row) for row in res))
    print(solve())