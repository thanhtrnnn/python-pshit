from os import path
import sys, math

# PYKT068
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
class Student:
    def __init__(self, id, name, examType) -> None:
        self.id = id
        self.name = name
        self.examType = examType
        
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + self.examType
    
a = [Student(input(), input(), input()) for _ in range(nint())]
for x in sorted(a, key = lambda x: x.id):
    print(x)