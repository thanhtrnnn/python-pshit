from os import path
from math import comb, sqrt, gcd, ceil, floor
import sys
from typing import Counter

# ICPC0108
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

def solve():
    n = nint()
    a = sorted(aint())
    cnt = 0

    for i in range(n - 1):
        j, k = i + 1, n - 1

        while j < k:
            total = a[i] + a[j] + a[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                cnt += 1
                j += 1

    print(cnt) # note: i do not trust this code, but its AC

t = int(input())
for _ in range(t):
    solve()

    # lena = nint()
    # a = aint()
    # res = 0 # set()

	# #1. Split nums into three lists: negative numbers, positive numbers, and zeros
    # neg, pos, zero = [], [], []
    # for num in a:
    #     if num > 0:
    #         pos.append(num)
    #     elif num < 0: 
    #         neg.append(num)
    #     else:
    #         zero.append(num)

    # #2. Create a separate set for negatives and positives for O(1) look-up times
    # N, P = Counter(neg), Counter(pos)

    # #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
    # #   i.e. (-3, 0, 3) = 0
    # if zero:
    #     for num in P:
    #         if -num in N:
    #             res += P[num] * N[-num] * len(zero) # res.add((-num, 0, num))

    # #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
    # if len(zero) >= 3:
    #     res += comb(len(zero), 3) # res.add((0,0,0))

    # #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
    # #   exists in the positive number set
    # for i in range(len(neg)):
    #     for j in range(i + 1, len(neg)): # still need list for neg and pos for random access
    #         target = -(neg[i] + neg[j])
    #         if target in P:
    #             res += P[target] # res.add(tuple(sorted([neg[i],neg[j],target])))

    # #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
    # #   exists in the negative number set
    # for i in range(len(pos)):
    #     for j in range(i + 1, len(pos)):
    #         target = -(pos[i] + pos[j])
    #         if target in N:
    #             res += N[target] # res.add(tuple(sorted([pos[i],pos[j],target])))

    # print(res) # printlist(res)

    