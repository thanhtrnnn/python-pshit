from os import path
import sys, math

# PY01044
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

s1, s2 = input().lower(), input().lower()
words1, words2 = s1.split(), s2.split()
union = sorted(set(words1) | set(words2)) # sorted(set(words1).union(set(words2)))
intersection = sorted(set(words1) & set(words2)) # sorted(set(words1).intersection(set(words2)))

print(*union)
print(*intersection)