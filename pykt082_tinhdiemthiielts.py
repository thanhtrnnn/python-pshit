from os import path
import sys, math

# PYKT082
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
def correctToBand(x):
    if x>38: return 9.0
    if x>36: return 8.5
    if x>34: return 8.0
    if x>32: return 7.5
    if x>29: return 7.0
    if x>26: return 6.5
    if x>22: return 6.0
    if x>19: return 5.5
    if x>15: return 5.0
    if x>12: return 4.5
    if x>9: return 4.0
    if x>6: return 3.5
    if x>4: return 3.0
    if x>2: return 2.5
    return 1.0

def roundBand(x):
    ext = x - int(x)
    if ext >= 0.75: 
        return int(x) + 1.0
    if ext >= 0.25: 
        return int(x) + 0.5
    return float(int(x))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

t = nint()
for _ in range(t):
    a = input().split()
    s = (correctToBand(int(a[0])) + correctToBand(int(a[1])) + float(a[2]) + float(a[3])) / 4
    print(roundBand(s))