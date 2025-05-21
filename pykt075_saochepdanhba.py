from os import path
import sys, math

# PYKT075
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

phonebook = []
with open('SOTAY.txt', mode = 'r') as f:
    data = [x.strip() for x in f.readlines()]
    n = len(data)
    day = data[0]    
    i = 1
    while i < n:
        info = [day.split()[-1], f'{data[i]}:', f'{data[i + 1]}']
        phonebook.append(info)
        i += 2
        if i < n and 'Ngay' in data[i]:
            day = data[i]
            i += 1

phonebook.sort(key = lambda x: (x[1].split()[-1], x[1].split()[0]))
with open('DIENTHOAI.txt','w') as f: 
    for x in phonebook: 
        line = f"{x[1]} {x[-1]} {x[0]}\n" 
        f.write(line)