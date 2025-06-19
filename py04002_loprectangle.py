from os import path
from stringprep import in_table_c21
import sys, math

# PY04002
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
class Rectangle:
    def __init__(self, a, b, c) -> None:
        self.width = a
        self.height = b
        self.color = c.capitalize()

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def color(self):
        return self.color.capitalize()

a = input().split()
if int(a[0]) > 0 and int(a[1]) > 0: 
    r = Rectangle(int(a[0]), int(a[1]), a[2]) 
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color))
else: 
    print('INVALID')
sys.exit()

# faulty int(arr[2]) in the original code, should be str
if __name__ == '__main__':
    t = int(input())
    while t:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
        t -= 1
