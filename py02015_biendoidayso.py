from os import path
import sys, math

# PY02015
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

def count(a):
    if a[0] == a[1] == a[2] == a[3]: 
        return 0
    
    res = [abs(a[i] - a[(i + 1) % 4]) for i in range(4)] # a[3] - a[0]
    return count(res) + 1

while True:
    a = aint()
    if a == [0] * 4: 
        break
    print(count(a))