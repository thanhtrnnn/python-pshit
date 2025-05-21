from os import path
import sys, math

# PY01025
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ','.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

s = input()
# first = len(s) % 3
# groups = [s[i:i+3] for i in range(first, len(s), 3)]
# if first:
#     groups.insert(0, s[:first])

# print(tostr(groups))
ans = s[-3:]
for i in range(len(s) - 3, 0, -3):
    ans=(s[i-3:i] if i >= 3 else s[:i]) + ',' + ans
    
print(ans)

