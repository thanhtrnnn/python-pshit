from os import path
import math, sys

# ICPC0101
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
res = len(a)
if n != 1:
    i = 0
    st = [0]
    while i < n:
        st.append(a[i])
        x, y = st.pop(), st.pop()
        if x and y and not (x ^ y) & 1:
            res -= 2
        else:
            st.append(y)
            st.append(x)
        i += 1

print(res) 