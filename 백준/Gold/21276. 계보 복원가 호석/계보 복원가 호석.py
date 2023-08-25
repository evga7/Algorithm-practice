# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
import bisect
import math
import re
import heapq
import sys
from collections import *
import itertools
import collections
si=sys.stdin.readline
#sys.setrecursionlimit(10 ** 6)
dx = [0,-1,0,1]  # 왼 위 오 아래
dy = [-1,0,1,0]
def input():return sys.stdin.readline().rstrip()
N=int(input())
arr=list(input().split())
indegree={cur:0 for cur in arr}
M=int(input())
graph={cur:[] for cur in arr}
m=dict()
r={cur:[] for cur in arr}
for i in range(M):
    a,b=input().split()
    graph[b].append(a)
    indegree[a]+=1
q=deque()
for cur in arr:
    if indegree[cur]==0:
        q.append(cur)
res1=[]
for cur in q:
    res1.append(cur)
while q:
    cur=q.popleft()
    for nxt in graph[cur]:
        indegree[nxt]-=1
        if not indegree[nxt]:
            q.append(nxt)
            r[cur].append(nxt)

res1.sort()
print(len(res1))
print(*res1)
arr.sort()
for cur in arr:
    s=cur + ' '+ str(len(r[cur]))
    print(s,end=' ')
    print(*sorted(list(r[cur])))
