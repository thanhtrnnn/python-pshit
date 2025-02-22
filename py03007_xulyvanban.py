from os import path
import re
import sys, math

# PY03007
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

para = sys.stdin.read
data = tostr(para().splitlines(), '')

# \s+ match any whitespace characters
# <= lookbehind that
# [.!?] match pattern
for sentence in re.split(r'[.!?]', data):
    if len(sentence) == 0:
        continue
    sentence = sentence.lower().split()
    sentence[0] = sentence[0].capitalize()
    print(tostr(sentence, ' '), ' ') # capitalize the first letter of the sentence
