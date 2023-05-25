# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
import re
import sys
from collections import *
import itertools
sys.setrecursionlimit(10 ** 6)
dx = [-1, 1, 0, 0]  # 위 아래 왼 오
dy = [0, 0, -1, 1]
N,M=map(int,input().split())
visited=[987654321]*100001
q=deque()
q.append((N,0))
m={}
visited[N]=0
while q:
    cur,cost=q.popleft()
    if cur==M:
        break
    for next in (cur*2,cur+1,cur-1):
        if 0<=next<=100000 and cost+1<visited[next]:
            visited[next]=cost+1
            m[next]=cur
            q.append((next,cost+1))
s=[]
MM=M
s.append(M)
while MM!=N :
    s.append(m[MM])
    MM=m[MM]
s.reverse()
print(visited[M])
for cur in s:
    print(cur,end=' ')


