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
dx = [0,-1,0,1]  # 왼 위 오 아래
dy = [-1,0,1,0]
N=int(si().rstrip())
visited=[0 for _ in range(20)]
arr=[list(map(int,si().rstrip().split())) for _ in range(N)]
res=float('inf')
def go(idx,cnt):
    if cnt==N//2:
        global res
        t1=0
        t2=0
        for i in range(N):
            for j in range(i+1,N):
                if visited[i] and visited[j]:
                    t1+=arr[i][j]+arr[j][i]
                elif not visited[i] and not visited[j]:
                    t2 += arr[i][j] + arr[j][i]
        res=min(res,abs(t1-t2))
        return
    for i in range(idx,N):
        if visited[i]:continue
        visited[i]=1
        go(i+1,cnt+1)
        visited[i]=0


go(0,0)
print(res)