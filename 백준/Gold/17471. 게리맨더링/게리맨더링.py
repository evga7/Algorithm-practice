# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
import re
import heapq
import sys
from collections import *
import itertools
import collections
si=sys.stdin.readline
#sys.setrecursionlimit(10 ** 6)
#dx = [0, 1, 0, -1]  # 오 아래 왼 위
#dy = [1, 0, -1, 0]
N=int(si().rstrip())
people=list(map(int,si().rstrip().split()))
city=[]
for i in range(N):
    temp=list(map(int,si().rstrip().split()))
    temp2=[]
    for j in range(1,len(temp)):
        temp2.append(temp[j]-1)
    city.append(temp2)
res=987654321
def city_sum(a):
    s=0
    for cur in a:
        s+=people[cur]
    return s
def chk(c):
    if not c:
        return False
    q=deque()
    chk=[0 for _ in range(N+1)]
    visited = [0 for _ in range(N + 1)]
    for cur in c:
        chk[cur]=1
    q.append(c[0])
    cnt=0
    visited[c[0]]=1
    while q:
        cnt+=1
        cur=q.popleft()
        for nxt in city[cur]:
            if chk[nxt] and not visited[nxt]:
                visited[nxt]=1
                q.append(nxt)
    if cnt==len(c):
        return True
    return False
def go(bit):
    global res
    a=[]
    b=[]
    for i in range(N):
        if bit & 1<<i:
            a.append(i)
        else:
            b.append(i)
    if a and b:
        ca=chk(a)
        cb=chk(b)
        if ca and cb:
            res=min(res,abs(city_sum(a)-city_sum(b)))

for i in range(1,1<<N):
    go(i)

if res==987654321:
    res=-1
print(res)