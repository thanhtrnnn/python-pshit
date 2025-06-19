from os import path
import sys
from math import sqrt, pi

# PYKT13039
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

a, b = map(float, input().split())

# hypotenuse of a right triangle
c = sqrt(a**2 + b**2)
# radius of incircle
r = (a + b - c) / 2
# length of bisector
x = sqrt((b - r) ** 2 + r * r)
# ratio between two longest radii, also the common ratio of all radii
# all radii form a geometric progression
k = (x - r) / (x + r)
# total area of the incircles/ triangle
p = (pi * r ** 2 / (1 - k ** 2)) / (a * b / 2)
print(f'{p:.4f}')


