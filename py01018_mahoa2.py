from os import path
import sys, math

# PY01018
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

P = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.") 
while True: 
    try: 
        k, s = sint()
    except: 
        break 
    k = int(k) 
    if k == 0: 
        break 

    res = [] 
    for i in s: 
        i = P.index(i)
        res.append(P[(i + k) % 28]) 
        
    print(*res[::-1], sep='')