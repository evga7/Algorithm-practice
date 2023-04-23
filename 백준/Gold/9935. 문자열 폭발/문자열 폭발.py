# N,M=map(int,input().split())
# visited=[[987654321]*M for _ in range(N)]
# arr=[list(map(int,input().strip())) for _ in range(N)]
# str=re.findall(r'\d+',str) 숫자만 때기
# re.findall(r'-?\d+', str1)] 음수는 이렇게
# word1 = re.findall("[a-zA-Z]+", st) 이건 문자 추출
#arr2 = [k[::-1] for k in zip(*arr)] 문자열 90도 회전
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
res=0
s=input()
ss=input()
last_ch=ss[len(ss)-1]
st=[]
for i in range(len(s)):
    cur=s[i]
    st.append(cur)
    if cur==last_ch:
        if ''.join(st[-len(ss):])==ss:
            del st[-len(ss):]
res=''.join(st)
if not res:
    res='FRULA'
print(res)