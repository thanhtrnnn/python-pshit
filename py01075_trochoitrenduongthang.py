from os import path
from math import sqrt, gcd, ceil, floor
import sys

# PY01075
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

t = nint()
# observation: gcd of the chosen cards is 1
# example:
# 6 3 11 9 -> gcd = 1 -> exists 6 * 1 - 3 * 1 - 11 * 1 + 9 * 1 = 1
for _ in range(t):
    min_cost = {0: 0} # gcd: cost
    b = [0] # reachable gcds
    n = nint()
    cards, costs = aint(), aint()

    for i in range(n):
        for p in b:
            curr_gcd = gcd(p, cards[i])
            curr_cost = min_cost[p] + costs[i]
            if curr_gcd not in min_cost:
                min_cost[curr_gcd] = curr_cost
                b.append(curr_gcd)
            elif min_cost[curr_gcd] > curr_cost:
                min_cost[curr_gcd] = curr_cost
    if 1 not in min_cost:
        min_cost[1] = -1
    
    print(min_cost[1])