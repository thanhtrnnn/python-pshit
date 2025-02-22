from os import path
from math import isqrt, gcd, ceil, floor
import re, sys

# PYKT073
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

n = nint()
poems = "".join(str(len(input().split())) for _ in range(n))
poems = poems.replace('7777', '2').replace('68', '1') 
poems = re.sub(r'1+', '1', poems)
# while '11' in poems: 
#     poems = poems.replace('11', '1') # 6868...68 -> 11...1 -> 1

print(len(poems), *poems, sep = '\n')

