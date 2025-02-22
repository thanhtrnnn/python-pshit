from os import path
from math import sqrt, gcd, ceil, floor
import sys

# idhere
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

def build_lps(pattern: str) -> list:
    # Array to store the longest proper prefix which is also a suffix
    lps = [0] * len(pattern)

    # Initialize tracking variables for prefix and current position
    current = 1
    prefix_length = 0
    while current < len(pattern):
        # If characters match, extend the prefix length
        if pattern[current] == pattern[prefix_length]:
            # Store the length of matching prefix
            prefix_length += 1
            lps[current] = prefix_length
            current += 1

        # If characters don't match and we're not at the start of the pattern
        elif prefix_length != 0:
            # Backtrack to the previous longest prefix-suffix
            prefix_length = lps[prefix_length - 1]

        # If no match and no prefix to backtrack
        else:
            # No prefix-suffix match found
            lps[current] = 0
            current += 1

    # Return the computed longest prefix-suffix array
    return lps

s = input()
print(*build_lps(s))