from datetime import datetime
from os import path
import sys, math

# PY04016
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
i = 1
class customer:
    def __init__(self, name, roomNo, checkIn, checkOut, additionalPrice):
        global i
        self.id = f'KH{str(i).zfill(2)}'
        self.name = name
        self.roomNo = roomNo
        self.floor = int(roomNo[0])
        self.stayingDays = (datetime.strptime(checkOut, '%d/%m/%Y') - datetime.strptime(checkIn, '%d/%m/%Y')).days + 1
        self.additionalPrice = additionalPrice
        i += 1
        
    def totalPrice(self):
        return self.stayingDays * (25 if self.floor == 1
                        else 34 if self.floor == 2
                        else 50 if self.floor == 3
                        else 80) + self.additionalPrice

    def __str__(self):
        return f'{self.id} {self.name} {self.roomNo} {self.stayingDays} {self.totalPrice()}'

# dates go with extra space in input
print(*sorted([customer(input(), input(), input().strip(), input().strip(), nint()) for _ in range(nint())], key=lambda x: -x.totalPrice()), sep='\n')