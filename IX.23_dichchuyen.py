from os import path
import sys, math

# IX.23
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

def same_line(points):
    n = len(points)
    if n <= 2:
        return True
    
    x1, y1 = points[0]
    x2, y2 = points[1]
    dx = x2 - x1
    dy = y2 - y1
    for i in range(2, n):
        x, y = points[i]
        if dx * (y - y1) - dy * (x - x1): # same as dx / (x - x1) != dy / (y - y1)
            return False
        
    return True

n = nint()
points = [aint() for _ in range(n)]

# bai nhu lon 
if not same_line(points):
    print('Yes')
    print('1 2 3')