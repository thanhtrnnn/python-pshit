from bisect import bisect_left
from os import path
from math import sqrt, gcd, ceil, floor
import sys

# idhere
input = lambda: sys.stdin.readline().rstrip("\r\n")
nint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
if path.exists("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt"):
    sys.stdin = open("E:/OneDrive - ptit.edu.vn/pro/dsa/input.txt", mode = 'r')
    sys.stdout = open("E:/OneDrive - ptit.edu.vn/pro/dsa/output.txt", mode = 'w')
###############################################
def lis(a):
    n = len(a)
    res = []
    for x in a:
        pos = bisect_left(res, x)
        if pos == len(res):
            res.append(x)
        else:
            res[pos] = x
    return len(res)

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
x0, y0 = a[0]
x1, y1 = a[1]

# Nếu đường thẳng không thẳng đứng (tức là x khác nhau)
if x0 != x1:
    # Duyệt các phao còn lại để kiểm tra có nằm trên cùng đường thẳng không
    found = False
    for i in range(2, n):
        xi, yi = a[i]

        # Kiểm tra 3 điểm (a[0], a[1], a[i]) có thẳng hàng không
        # Sử dụng so sánh chéo để tránh chia (tránh sai số)
        if (y1 - y0) * (xi - x0) != (yi - y0) * (x1 - x0):
            print('Yes')
            # In ra chỉ số 3 phao không thẳng hàng (theo thứ tự 1-based)
            print(1, 2, i + 1)
            found = True
            break

    # Nếu tất cả các phao đều thẳng hàng
    if not found:
        print('No')

# Trường hợp đường thẳng đứng (x0 == x1)
else:
    found = False
    for i in range(2, n):
        xi, yi = a[i]
        # Nếu tồn tại phao có x khác x0 thì không thẳng hàng
        if xi != x0:
            print('Yes')
            print(1, 2, i + 1)
            found = True
            break

    if not found:
        print('No')