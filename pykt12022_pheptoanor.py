from os import path
import sys, math

# PYKT12022
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

n = nint()
a = aint()
seq, res = set(), set()

for x in a:
    curr_seq = set()
    res.add(x)
    seq.add(x)

    for y in seq:
        curr_seq.add(x | y)
        res.add(x | y)

    seq = curr_seq
    
print(len(res))