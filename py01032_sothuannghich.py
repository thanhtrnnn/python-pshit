from os import path
import sys, math

# PY01032
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

a, b, m = mint()
if m > 3:
    print(sum([1 for i in [0, 1] if a <= i <= b]))

elif m == 3:
    print(sum([1 for i in [0, 1, 6643, 1422773, 5415589] if a <= i <= b]))

elif m == 2:
    res = 0
    for i in range(1, 10000):
        s1 = bin(i)[2:]
        s2 = ''.join(reversed(s1))  
        arr = [s1 + s2, s1 + '0' + s2, s1 + '1' + s2] # generate possible profiles
        for j in arr:
            x = int(j, 2)
            if a <= x <= b: 
                res += 1

    res += sum([1 for i in [0, 1] if a <= i <= b])
    print(res)