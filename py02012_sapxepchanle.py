from os import path
import sys, math

# PY02012
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

n = nint()
a = []
while len(a) < n:
    a.extend(aint())

odd = []
even = []
for x in a:
    if x % 2:
        odd.append(x)
    else:
        even.append(x)

odd.sort(reverse = True)
even.sort()
i, j = 0, 0
for x in a:
    if x % 2:
        print(odd[j], end=' ')
        j += 1
    else:
        print(even[i], end=' ')
        i += 1