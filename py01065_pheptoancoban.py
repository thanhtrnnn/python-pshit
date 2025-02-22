from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY01065
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
def printlist(a): print(' '.join(map(str, a)))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

def possiblenum(s):
    undefined = []
    if s[0] == '?':
        for i in range(1, 10):
            undefined.append(str(i) + s[-1])
    else:
        undefined.append(s)

    nums = []
    if s[-1] == '?':
        for x in undefined:
            for i in range(10):
                nums.append(x[0] + str(i))
    else:
        nums = undefined
    
    return nums

def possibleopr(s):
    return '+-*/' if s == '?' else s # actually '+-' is enough, * and / wont work for 2-digit numbers

def eval(a, opr, b, c):
    if opr == '+':
        return a + b == c
    if opr == '-':
        return a - b == c
    if opr == '*':
        return a * b == c
    if a % b == 0:
        return a // b == c
    return False

def solve(): 
    exp = input().split()
    x = possiblenum(exp[0])
    opr = possibleopr(exp[1])
    y = possiblenum(exp[2])
    ans = possiblenum(exp[-1])
    
    for i in x:
        for op in opr:
            for k in y:
                for anz in ans:
                    if eval(int(i), op, int(k), int(anz)):
                        print(f'{i} {op} {k} = {anz}')
                        return
    
    print('WRONG PROBLEM!')

t = nint()
for _ in range(t):
    solve()
    # exp = input().split()
    # x = possiblenum(exp[0])
    # opr = possibleopr(exp[1])
    # y = possiblenum(exp[2])
    # ans = possiblenum(exp[-1])
    # found = False
    
    # for i in x:
    #     for op in opr:
    #         for k in y:
    #             for anz in ans:
    #                 if eval(int(i), op, int(k), int(anz)):
    #                     res = f'{i} {op} {k} = {anz}'
    #                     found = True
    #                     break
    #             if found:
    #                 break
    #     if found:
    #         break

    
    # print(res if res else 'WRONG PROBLEM!')