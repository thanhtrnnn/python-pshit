from collections import defaultdict
from os import path
import sys, math

# PYKT2049
input = lambda: sys.stdin.readline().rstrip("\\r\\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
# Check if running locally and redirect stdin/stdout if input/output files exist
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################
n = nint() # Read the number of operations

# Union-Find (Disjoint Set Union - DSU) data structure
# parent array stores the parent of each element.
# If parent[i] is negative, then i is a root, and -parent[i] is the size of the set.
parent = [-1] * (n + 1) # Initialize parent array for n+1 elements (1-indexed)

# Find operation: returns the representative (root) of the set containing x
# Uses path compression for optimization.
def find(x):
    if parent[x] < 0: # If x is a root (parent[x] is negative)
        return x
    # Path compression: make all nodes on the path point directly to the root
    parent[x] = find(parent[x])
    return parent[x]

# Union operation (naive version, can lead to TLE due to skewed trees)
def union(x, y): # TLE
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY: # Only union if they are in different sets
        parent[rootX] = rootY # Make rootX a child of rootY

# Merge operation (optimized union by rank/size)
# Merges the sets containing x and y.
# Uses union by size (or rank) to keep the tree flat.
def merge(x, y):
    x_root = find(x) # Find the root of the set containing x
    y_root = find(y) # Find the root of the set containing y

    if x_root == y_root: # If x and y are already in the same set
        return
    
    # Union by size: attach the smaller tree to the root of the larger tree
    # parent[root] stores the negative of the size of the set if it's a root.
    if parent[y_root] < parent[x_root]: # If size of y_root's set is larger
        x_root, y_root = y_root, x_root # Swap to make x_root the larger set's root
    
    parent[x_root] += parent[y_root] # Add size of y_root's set to x_root's set
    parent[y_root] = x_root # Make y_root a child of x_root

# Process n operations
for i in range(n):
    x, y, z = mint() # Read x, y, and operation type z
    if z == 1: # If operation is to merge/union sets containing x and y
        merge(x, y) # Use the optimized merge operation
    else: # If operation is to check if x and y are in the same set
        # Print 1 if they are in the same set (have the same root), 0 otherwise
        print(1 if find(x) == find(y) else 0)

# DFS (TLE) - Commented out, as it's not the primary solution used
# def dfs(u):
#     visited[u] = True
#     for v in adj[u]:
#         if not visited[v]: 
#             dfs(v)

# adj = defaultdict(list)
# for i in range(n):
#     u, v, op = mint()
#     if op == 1:
#         adj[u].append(v)
#         adj[v].append(u)
#     else:
#         visited = [False] * (n + 1)
#         dfs(u)
#         print(1 if visited[v] else 0)