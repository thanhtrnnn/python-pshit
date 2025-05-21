from os import path
import sys, math

# PYKT097
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a, s: s.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

for sentence in sys.stdin:
    if len(sentence) == 0:
        continue
    sentence = sentence.lower().split()
    sentence[0] = sentence[0].capitalize()

    if '.!?'.count(sentence[-1]):
        sentence[-2] += sentence[-1]
        sentence.pop()
    elif not '.!?'.count(sentence[-1][-1]):
        sentence[-1] += '.'
        
    print(tostr(sentence, ' '))