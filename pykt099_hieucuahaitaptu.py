from os import path
import sys, math

# PYKT099
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

sys.stdin = open("DATA1.in", mode = 'r')
s1 = set(sys.stdin.read().lower().split())
sys.stdin = open("DATA2.in", mode = 'r')
s2 = set(sys.stdin.read().lower().split())

print(*sorted(s1.difference(s2)))
print(*sorted(s2.difference(s1)))
