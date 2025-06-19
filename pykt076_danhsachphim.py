from os import path
import sys, math
from datetime import datetime

# PYKT076
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
class Movie:
    def __init__(self, id, genre, releaseDate, title, episodes):
        self.id = f'P{str(id).zfill(3)}'
        self.genre = genre
        self.releaseDate = releaseDate
        self.title = title
        self.episodes = episodes

n, m = mint()
genre = {}
for i in range(1, n + 1):
    genreName = input()
    genre[f'TL{str(i).zfill(3)}'] = genreName

db = [Movie(currId, genre[input()], input(), input(), nint()) for currId in range(1, m + 1)]
db.sort(key=lambda x: (datetime.strptime(x.releaseDate, "%d/%m/%Y"), x.title, -x.episodes))
for movie in db:
    print(movie.id, movie.genre, movie.releaseDate, movie.title, movie.episodes)
