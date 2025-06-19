### CHỈ CẦN RA VÀO FILE -> COPY ĐẾN DÒNG 7
from os import path
import sys, math

if path.exists("input.txt"):
    sys.stdin = open("input.txt", mode = 'r')
    sys.stdout = open("output.txt", mode = 'w')


input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))

t = nint()
for _ in range(t):
    n = nint()
    a = aint()
    