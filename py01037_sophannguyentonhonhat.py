from bisect import bisect_left
# from os import path
import sys

# PY01037
input = lambda: sys.stdin.readline()
nint = lambda: int(input())
# mint = lambda: map(int, input().split())  
# sint = lambda: map(str, input().split())
# aint = lambda: list(map(int, input().split()))
# def printlist(a): print(' '.join(map(str, a)))
# def fileio():
#     sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
#     sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

# if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
#     fileio()

a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
for _ in range(nint()):
    n = int(nint())
    print(a[bisect_left(a, n)])
