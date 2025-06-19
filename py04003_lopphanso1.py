from os import path
import sys, math

# PY04003
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

    def __str__(self):
        return f'{self.a}/{self.b}'
    
tu, mau = mint()
print(fraction(tu, mau))