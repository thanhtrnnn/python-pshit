from os import path
import sys, math

# PYKT094
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
def cleanName(s):
    return s.lower().capitalize()

def salaryCoef(s):
    y = int(s[1:3])
    if 1 <= y <= 3:
        if s[0] == 'A': 
            return 10
        elif s[0] == 'B': 
            return 10
        elif s[0] == 'C': 
            return 9
        return 8
    elif 4 <= y <=8:
        if s[0] == 'A': 
            return 12
        elif s[0] == 'B': 
            return 11
        elif s[0] == 'C': 
            return 10
        return 9
    elif 9 <= y <= 15:
        if s[0] == 'A': 
            return 14
        elif s[0] == 'B': 
            return 13
        elif s[0] == 'C': 
            return 12
        return 11
    else: 
        if s[0] == 'A': 
            return 20
        elif s[0] == 'B': 
            return 16
        elif s[0] == 'C': 
            return 14

        return 13
class department:
    def __init__(self, s) -> None:
        s = s.split()
        self.id = s[0]
        self.name = ' '.join(s[1:])

class staff:
    def __init__(self, id, name, sday, days, o) -> None:
        self.id = id
        self.name = name
        self.sum = sday * days * salaryCoef(id)*10**3
        self.o = o
    def __str__(self) -> str:
        return self.id + '  ' + self.name + ' ' + self.o.name + ' ' + str(self.sum)
    
m = {}
for i in range(nint()):
    o = department(input())
    m[o.id] = o

a = []
for i in range(nint()): 
    id = input()
    a.append(staff(id, input(), nint(), nint(), m[id[3:]]))

print('\n'.join(str(i) for i in a))
