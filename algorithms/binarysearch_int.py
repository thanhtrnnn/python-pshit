from os import path
import sys, math

# idhere
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
def condition(value):
    pass

def bs(a):
    ok = 0  
    ng = len(a) # impossible value
    while abs(ok - ng) > 1: 
        mid = (ok + ng) // 2
        if condition(mid): 
            ok = mid
        else:
            ng = mid
    return ok

def binary_search(array) -> int:
    left, right = 0, len(array) # [left, right] range of possible answers
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

t = nint()
for _ in range(t):
    n = nint()
    a = aint()
