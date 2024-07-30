from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
a=[list(map(int,input().split())) for _ in range(5)]
c=[[0 for _ in range(5)] for _ in range(5)]
row=[0 for _ in range(5)]
col=[0 for _ in range(5)]
xx=[0 for _ in range(2)]
m=defaultdict(int)
bin_cnt=0
m2=defaultdict(int)
def go():
    global bin_cnt
    l_b=0
    r_b=0
    for i in range(5):
        if row[i]==32:
            continue
        if not xx[0] and c[i][i]:
            l_b+=1
        if not xx[1] and c[i][4-i]:
            r_b+=1
        for j in range(5):
            if c[i][j]:
                if not (row[i] & (1<<j)):
                    row[i]+=(1<<j)
                    if row[i]==31:
                        bin_cnt+=1
            if c[j][i]:
                if not (col[i] & (1<<j)):
                    col[i]+=(1<<j)
                    if col[i]==31:
                        bin_cnt+=1
    if l_b==5:
        xx[0]=1
        bin_cnt+=1
    if r_b==5:
        xx[1]=1
        bin_cnt+=1

for i in range(5):
    for j in range(5):
        m[a[i][j]]=(i,j)
idx=0
m2["row"]=0
m2["col"]=5
m2["x"]=10
for i in range(5):
    b=list(map(int,input().split()))
    for cur in b:
        idx+=1
        x,y=m[cur]
        c[x][y]=1
        go()
        if bin_cnt>=3:
            print(idx)
            exit(0)