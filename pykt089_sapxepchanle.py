import math, sys
from os import path

# PYKT089
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

n = nint()
a = aint()
while len(a) < n: 
    a.extend(aint())

# odd = []
# even = []
# for x in a:
#     odd.append(x) if x % 2 else even.append(x)

# odd.sort(reverse=True)
# even.sort()

# alternative:
odd = sorted((x for x in a if x % 2), reverse=True)
even = sorted(x for x in a if x % 2 == 0)

# iterator
i, j = 0, 0

for x in a:
    if x % 2:
        print(odd[i], end=' ')
        i += 1
    else:
        print(even[j], end=' ')
        j += 1

