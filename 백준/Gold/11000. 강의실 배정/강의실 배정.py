# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전

# p = [i for i in range(N + 1)]
# def find(x):
#     if p[x] == x:
#         return x
#     p[x] = find(p[x])
#     return p[x]
# def uni(x, y):
#     x = find(x)
#     y = find(y)
#     if x != y:
#         if x < y:
#             p[y] = x
#         else:
#             p[x] = y
#         return True
#     return False
#dx = [-1,0]  # 오 왼 위 아
#dy = [0,-1]
import heapq
import itertools
import math
from collections import *
import bisect
import re
import sys
sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9)
def is_inside(x, y, N, M):
    return 0 <= x < N and 0 <= y < M
# dx=[0,1,0,-1,-1,-1,1,1]
# dy=[1,0,-1,0,-1,1,1,-1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N=int(input())
a=[list(map(int,input().split())) for _ in range(N)]
m=defaultdict(int)
st=set()
for s,e in a:
    m[s]+=1
    m[e]-=1
    st.add(s)
    st.add(e)
b=sorted(list(st))
cnt=0
res=0
for cur in b:
    cnt+=m[cur]
    res=max(res,cnt)
print(res)
    