from os import path
import sys, math
from decimal import Decimal, ROUND_HALF_UP

# PY04014
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(Decimal, input().split())) # for floating point scores
tostr = lambda a: ' '.join(map(str, a))
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################
class student:
    def __init__(self, id, name, scoreboard):
        self.id = f'HS{str(id).zfill(2)}'
        self.name = name
        self.scoreboard = scoreboard
        self.avgScore = (scoreboard[0] * 2 + scoreboard[1] * 2 + sum(scoreboard[2:])) / 12
        self.avgScore = self.avgScore.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        self.eval = 'XUAT SAC' if self.avgScore >= 9 else \
                    'GIOI' if self.avgScore >= 8 else \
                    'KHA' if self.avgScore >= 7 else \
                    'TB' if self.avgScore >= 5 else \
                    'YEU'
    def __str__(self):
        return f'{self.id} {self.name} {self.avgScore:.1f} {self.eval}'
        
students = sorted([student(i + 1, input(), aint()) for i in range(nint())], key=lambda x: (-x.avgScore, x.id))
print('\n'.join(map(str, students)))
