import math, sys
from os import path

# PY02029

def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

n, m = map(int, input().split())
a = list(map(int, input().split()))
counter = dict.fromkeys(a, 0)
for i in range(n):
    counter[a[i]] += 1
out = sorted(counter.items(), key = lambda elem: elem[1], reverse = True)

tmp = 0
second = False
for elem in out:
    if second and tmp != elem[1]:
        print(elem[0])
        second = False
        break
    second = True
    tmp = elem[1]

if (second): 
    print('NONE')
