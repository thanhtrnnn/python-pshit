from os import path
import sys, math

# PY02075
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

t = nint()
for _ in range(t):
    n = nint()
    # line ends asap
    lines = sorted([aint() for _ in range(n)], key=lambda x: x[1])
    
    res, prevend = 0, -1
    for start, end in lines:
        if start >= prevend:  # If the current line starts after or when the previous one ends
            res += 1
            prevend = end  # Update the end of the last counted line

    print(res)  # Output the count of non-overlapping lines