from os import path
import sys, math

# PY04006
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

def distance(a, b): 
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def area(a, b, c):
    return math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c)) / 4

t = nint()
lines = []
for _ in range(t):
    lines.extend(list(map(float, input().split())))
    
i = 0 
for j in range(t):
    a = distance([lines[i], lines[i+1]], [lines[i+2], lines[i+3]])
    b = distance([lines[i+2], lines[i+3]], [lines[i+4], lines[i+5]])
    c = distance([lines[i+4], lines[i+5]], [lines[i], lines[i+1]])
    i += 6
    if max([a, b, c]) * 2 >= a + b + c: 
        print('INVALID')
    else: 
        print(f'{round(area(a, b, c), 2):.2f}')
