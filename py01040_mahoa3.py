from os import path
import sys, math

# PY01040
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ''.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

def rotate(s):
    xum = sum(ord(c) - ord('A') for c in s)
    return tostr(chr((ord(c) - ord('A') + xum) % 26 + ord('A')) for c in s)

t = nint()
for _ in range(t):
    s = input()
    left, right = rotate(s[:len(s) // 2]), rotate(s[len(s) // 2:])
    
    res = ''
    for i in range(len(left)):
        offset = ord(right[i]) - ord('A')
        res += chr((ord(left[i]) - ord('A') + offset) % 26 + ord('A'))

    print(res)
