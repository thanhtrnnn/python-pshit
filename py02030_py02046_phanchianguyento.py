from os import path
import sys, math

# PY02030, PY02046
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

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = nint()
b = []
for x in aint():
    if not b.count(x):
        b.append(x)

n = len(b)
for i in range(1, n):
    b[i] += b[i - 1]

res = -1
for i in range(n):
    if isPrime(b[i]) and isPrime(b[-1] - b[i]):
        res = i
        break
print(res if res != -1 else 'NOT FOUND')