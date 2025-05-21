from os import path
import sys, math

# PYKT12009
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(float, input().split())) # int TLE trololing
tostr = lambda a: ' '.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

def kadane(x):
    sum_pos, max_sumpos, sum_neg, min_sumneg = 0.0, 0.0, 0.0, 0.0
    
    for i in a:
        sum_pos += i - x
        sum_neg += i - x

        if sum_pos > 0.0:
            if max_sumpos < sum_pos:
                max_sumpos = sum_pos
        else: 
            sum_pos = 0.0

        if sum_neg < 0.0:
            if min_sumneg > sum_neg:
                min_sumneg = sum_neg
        else:
            sum_neg = 0.0

    return round(max_sumpos, 6), round(-min_sumneg, 6)    

n = nint()
a = aint()
pos, neg = 1.0, 0.0
l, r = min(a), max(a)
while pos != neg:
    mid = (l + r) / 2
    pos, neg = kadane(mid)
    if pos > neg:
        l = mid
    else:
        r = mid

print(f'{pos:.6f}')