from datetime import datetime
from os import path
import sys, math

# PYKT077
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
class ExamInfo:
    def __init__(self, id, subjectId, date, time, group):
        self.id = f'T{str(id).zfill(3)}'
        self.subjectId = subjectId
        self.subjectName = subjects[subjectId]
        self.date = date
        self.time = time
        self.group = group

n, m = mint()
subjects = {}
for i in range(1, n + 1):
    subjectId, subjectName = input(), input()
    subjects[subjectId] = subjectName

db = []
for currId in range(1, m + 1):
    exam = input().split()
    db.append(ExamInfo(currId, exam[0], exam[1], exam[2], exam[3]))

db.sort(key=lambda x: (datetime.strptime(x.date, "%d/%m/%Y"), x.time, x.id))
for exam in db:
    print(exam.id, exam.subjectId, exam.subjectName, exam.date, exam.time, exam.group)