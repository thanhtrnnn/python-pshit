from os import path
import sys, math

# PY04004
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

class fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = math.gcd(self.a, self.b)
        self.a //= x
        self.b //= x
    
    def __add__(self, other):
        tu = self.a * other.b + other.a * self.b
        mau = self.b * other.b
        return fraction(tu, mau)

    def __str__(self):
        return f'{self.a}/{self.b}'
    
tu1, mau1, tu2, mau2 = mint()
p1, p2 = fraction(tu1, mau1), fraction(tu2, mau2)
print(p1 + p2)