# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
import re
import heapq
import sys
from collections import *
import itertools
sys.setrecursionlimit(10 ** 5)
#input=sys.stdin.readline()
dx = [-1, 1, 0, 0]  # 위 아래 왼 오
dy = [0, 0, -1, 1]
N,M=map(int,input().split())
visited=[[[[0]*21 for _ in range(21)] for _ in range(21) ]for _ in range(21)]
arr=[]
for i in range(N):
    arr.append(list(input()))
for i in range(N):
    for j in range(M):
        arr[i][j]=1<<(ord(arr[i][j])-ord('A'))

res=0
def go(x,y,cost,bit):
    global res
    res=max(res,cost)
    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]
        if 0<=n_x<N and 0<=n_y<M:
            c= arr[n_x][n_y]
            if not bit & c:
                go(n_x,n_y,cost+1,bit|c)
go(0,0,1,arr[0][0])

print(res)