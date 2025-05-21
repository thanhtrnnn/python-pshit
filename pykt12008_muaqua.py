from os import path
import sys, math

# PYKT12008
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
sint = lambda: map(str, input().split())
aint = lambda: list(map(int, input().split()))
tostr = lambda a: ' '.join(map(str, a))
def fileio():
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################

if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    fileio()

n, ppl, lim = mint()
gifts = [0] + aint()

n_ti = nint()
ti = [x for x in aint() if 0 < x <= n] # list(map(int, filter(lambda x: 0 < int(x) <= n, input().split())))
n_teo = nint()
teo = [x for x in aint() if 0 < x <= n]
n_ti, n_teo = len(ti), len(teo)

if ppl < lim or n < lim or n < ppl or (lim > n_ti or lim > n_teo):
    print(-1)
else:
    demand = sorted(set(ti).intersection(teo), key = lambda x: gifts[x])
    ti.sort(key = lambda x: gifts[x])
    teo.sort(key = lambda x: gifts[x])

    taken = max(0, 2 * lim - ppl)
    res = 0
    if taken > len(demand):
        print(-1)

    ti_mua, teo_mua = set(demand), set()
    total = 0
    for i in range(taken):
        if demand[i] not in teo_mua:
            total += gifts[demand[i]]
            teo_mua.add(demand[i])
            gifts[demand[i]] = -1
            lim -= 1
            ppl -= 1

    curr_ti, curr_teo = lim, lim

    for i in range(n_ti):
        if curr_ti <= 0: 
            break
        if ti[i] not in teo_mua:
            total += gifts[ti[i]]
            teo_mua.add(ti[i])
            if ti[i] in ti_mua:
                curr_teo -= 1
            gifts[ti[i]] = -1
            curr_ti -= 1
            ppl -= 1

    for i in range(n_teo):
        if curr_teo <= 0:
            break
        if teo[i] not in teo_mua:
            total += gifts[teo[i]]
            teo_mua.add(teo[i])
            gifts[teo[i]] = -1
            curr_teo -= 1
            ppl -= 1

    if curr_ti or curr_teo: 
        print(-1)
    else:
        adj = sorted([(gifts[i], i) for i in range(1, n + 1)]) 
        for i in range(1, n + 1):
            if ppl <= 0:
                break
            if adj[i][1] not in teo_mua:
                total += adj[i][0]
                teo_mua.add(adj[i][1])
                ppl -= 1

    print(total if not ppl else -1)