from os import path
import sys, math

# PY04015
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
class customer:
    def __init__(self, no, name, old, neo) -> None:
        self.id = f'KH{str(no).zfill(2)}'
        self.name = name
        m = neo - old

        if m > 100: 
            self.total = ((m - 100) * 200 + 50 * (100 + 150)) * 1.05
        elif m > 50: 
            self.total = ((m - 50) * 150 + 50 * 100) * 1.03
        else: 
            self.total = m * 102

a = [customer(t, input(), nint(), nint()) for t in range(1, nint() + 1)]
a = sorted(a, key = lambda x: (-x.total, x.id))

for x in a: 
    print(x.id, x.name, f'{x.total:.0f}')
