from os import path
import sys, math

# PYKT090
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

# if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
#     fileio()
sys.stdin = open("CONTACT.in", mode = 'r')

a = set()
while True:
    s = input()
    if not s:
        break
    a.add(s.lower())

print(*sorted(a), sep = '\n')