from os import path
import sys, math

# ICPC0110
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
# bai sieu cap nhu lon cam on god nyagami
c, e = 0, -10**9
for t in range(nint()):
    input()
    a = input()
    x, y, z = e, e, e
    n = len(a) // 3
    while a[n] != ' ': 
        n -= 1
    first = a[:n]
    a = a[n:]

    for i in map(int, first.split()): 
        if i >= x:
            z, y, x = y, x, i
        elif i >= y:
            z, y = y, i
        elif i > z: 
            z = i

    n = len(a) >> 1
    while a[n] != ' ': 
        n -= 1
    for i in map(int, a[:n].split()):
        if i <= z: 
            continue
        if i >= x:
            z, y, x = y, x, i
        elif i >= y:
            z, y = y, i
        else: 
            z = i

    for i in map(int, a[n:].split()):
        if i >= x:
            z, y, x = y, x, i
        elif i >= y:
            z, y = y, i
        elif i > z: 
            z = i
        
    print(x + y + z)
