from os import path
import sys, math

# PYKT12006
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

n, k = mint()
a = aint()
b = aint()
prices = [(a[i], b[i]) for i in range(n)]
prices.sort(key = lambda x: x[0] - x[1])

res = sum(prices[i][0] for i in range(k))
i = k
while i < n and prices[i][0] < prices[i][1]:
    res += prices[i][0]
    i += 1
    
res += sum(prices[i][1] for i in range(i, n))

print(res)