from os import path
import sys, math

# PY03016
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

n = nint()
a = [nint() for _ in range(n)]
st = []
res = 0

for x in a:
    curr = 1
    while st and st[-1][0] < x:
        res += st[-1][1]
        st.pop()
    
    if st:
        topx, topcurr = st[-1]
        if topx == x:
            curr = topcurr + 1
            res += topcurr
            st.pop()
            res += 1 if st else 0
        else:
            res += 1
    st.append((x, curr))

print(res)
