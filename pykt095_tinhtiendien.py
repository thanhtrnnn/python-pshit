from os import path
import sys, math

# idhere
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str.capitalize, a))
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################
class customer:
    def __init__(self, id, name, type, old, neo):
        self.id = f'KH{str(id).zfill(2)}'
        self.name = tostr(name.lower().split())
        nums = neo - old
        lim = 100 if type == 'A' else \
                500 if type == 'B' else 200
        
        self.inner = nums * 450 if nums <= lim else \
                    lim * 450
        
        self.over = 0 if nums <= lim else \
                    (nums - lim) * 1000
        
        self.vat = int(max(0, self.over) * 0.05)
        self.total = self.inner + self.over + self.vat
    
    def __str__(self):
        return f'{self.id} {self.name} {self.inner} {self.over} {self.vat} {self.total:.0f}'

a = [customer(t + 1, input(), (line := input().split())[0], int(line[1]), int(line[2])) for t in range(nint())]
a.sort(key=lambda x: (-x.total, x.id))
print(*a, sep='\n')