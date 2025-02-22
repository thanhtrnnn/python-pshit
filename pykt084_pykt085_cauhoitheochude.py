from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PYKT084
input = lambda: sys.stdin.readline().rstrip("\r\n")
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

n = nint()
topics = {} 
ques = [] 
for i in range(n): 
    s = input() 
    if s: 
        ques.append(s) 
        topics[ques[0]] = topics.get(ques[0], 0) + 1
    else: 
        ques.clear() 
        
for key in topics: 
    print(f"{key}: {topics[key] - 1}") # discard the topic name