from os import path
import sys, math
from datetime import date

# PY04013
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

a = {}
def minute(s):
    h, m = s.split(':')
    return int(h) * 60 + int(m)

class city:
    def __init__(self, n, start, end, m):
        self.code = ''
        self.name = n
        self.water = m
        self.time = minute(end) - minute(start)
    def __str__(self):
        return f'{self.code} {self.name} {self.water / (self.time / 60):.2f}'

i = 1
for _ in range(nint()):
    x = city(input(), input(), input(), nint())
    if x.name not in a:
        x.code = f'T{str(i).zfill(2)}'
        i += 1
        a[x.name] = x
    else:
        a[x.name].time += x.time
        a[x.name].water += x.water

print(*a.values(), sep='\n')