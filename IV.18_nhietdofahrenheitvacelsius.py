from os import path
import sys, math

# IV.18
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

t = input()
deg = t[-1].lower()
if deg == 'c':
    res = float(t[:-1]) * 9 / 5 + 32
else:
    res = (float(t[:-1]) - 32) * 5 / 9
    
print(f'{res:.2f}C' if deg == 'f' else f'{res:.2f}F')