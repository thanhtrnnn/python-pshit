from os import path
import sys, math

# idhere
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

# if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    # fileio()
sys.stdin = open("VANBAN.in", mode = 'r')

maxlen = 0
res = []
while True:
    line = input()
    if not line:
        break

    for word in line.split():
        if word == word[::-1]:
            if len(word) > maxlen:
                maxlen = len(word)
                res = [[word, 1]]
            elif len(word) == maxlen:
                for x in res:
                    if x[0] == word:
                        x[1] += 1
                        break
                else:
                    res.append([word, 1])

for x in res:
    print(x[0], x[1])

