from os import path
import sys, math

from numpy import char

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
def countSetBits(n):
    count = 0
    for i in range(32):
        if n & (1 << i):
            count += 1
    return count

def isPowerOfTwo(n):
    # check if more than 1 set bit
    # return not n & (n - 1) # include 0
    return n != 0 and (not (n & (n - 1))) # exclude 0

def charTransform():
    # char(1 << 5) = ' '
    print(chr(ord('A') | (1 << 5))) # to lowercase
    print(chr(ord('a') & ~(1 << 5))) # to uppercase
    print(chr(ord('c') & ord('_'))) # '_' = 95
    print(ord('A') & 31, ord('c') & 31) # position in alphabet, 31 = 11111(2)

def countDiffChars(s):
    mask = 0
    for c in s:
        mask |= 1 << (ord(c) - ord('a'))
    return mask.bit_count()

def xorSwap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return tostr([a, b])

def clearSetBits(n, i):
    return n & (~((1 << (i + 1)) - 1))

def uses(a, b):
    # set operations
    union = a | b
    intersect = a & b
    subtract = a & ~b
    negation = ~a

    bitset = a | (1 << 5) # set bit 5
    bitclear = a & ~(1 << 5) # clear bit 5
    lastbit = a & -a # a & ~(a - 1), x ^ (x & (x - 1)) # lowest set bit by weight (1, 2, 4, 8, ...)

def grayCode(n):
    # 0 ^ 1 = 1, 1 ^ 1 = 0
    a = [i ^ (i >> 1) for i in range(1 << n)]
    return a

def reverseGrayCode(g):
    n = 0
    while g:
        n ^= g
        g >>= 1
    return n

def findAllSubsets(a):
    n = len(a)
    result = []

    for i in range(1 << n):
        subset = []
        for j in range(n):
            # check if jth bit is set in i
            if i & (1 << j):
                subset.append(a[j])
        result.append(subset)

    return result

for i in range(50):
    if isPowerOfTwo(i):
        print(i, end = ' ')
print()

# charTransform()
print(xorSwap(5, 7))
print(clearSetBits(31, 2)) # 11111 -> 11000 = 24
print(countDiffChars('abac')) # 3
print(*grayCode(2)) # 3
print(isPowerOfTwo(0))
