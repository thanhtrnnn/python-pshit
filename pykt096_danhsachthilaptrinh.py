from os import path
import sys, math

# idhere
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
class contestant:
    def __init__(self, id, name, teamid):
        self.id = f'C{str(id).zfill(3)}'
        self.name = name
        self.uni = teammap[teamid][1]
        self.team = teammap[teamid][0]

    def __str__(self):
        return f'{self.id} {self.name} {self.team} {self.uni}'
    
n = nint()
teammap = {f'Team{str(i).zfill(2)}': (input(), input()) for i in range(1, n + 1)}
a = [contestant(i + 1, input(), input()) for i in range(nint())]
a.sort(key=lambda x: (x.name))
print(*a, sep='\n')