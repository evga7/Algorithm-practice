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
arr=list(map(int,input().split()))
st=[]
res=[0 for _ in range(N+1)]
res2=[100001 for _ in range(N+1)]
for i,cur in enumerate(arr):
    if not st:
        st.append(i)
    else:
        while st and cur>=arr[st[-1]]:
            st.pop()
        res[i]+=len(st)
        if st:
            if res2[i]==100001:
                res2[i]=st[-1]
        st.append(i)

st=[]
for i in range(N-1,-1,-1):
    cur=arr[i]
    if not st:
        st.append(i)
    else:
        while st and cur>=arr[st[-1]]:
            st.pop()
        res[i]+=len(st)
        if st:
            if res2[i]==100001:
                res2[i]=st[-1]
            else:
                dist=abs(st[-1]-i)
                dist2=abs(res2[i]-i)
                if dist==dist2:
                    res2[i]=min(res2[i],st[-1])
                else:
                    if dist<dist2:
                        res2[i]=st[-1]
        st.append(i)
for i in range(N):
    if res2[i]!=100001:
        print(res[i],res2[i]+1)
    else:
        print(res[i])