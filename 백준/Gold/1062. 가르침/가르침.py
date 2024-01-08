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
import collections
si=sys.stdin.readline
#dx = [0, 1, 0, -1]  # 오 아래 왼 위
#dy = [1, 0, -1, 0]
N,M=map(int,si().rstrip().split())
arr=[si().rstrip() for _ in range(N)]
bit_arr=[]
for cur in arr:
    bb=0
    for i in range(len(cur)):
        bb|=1<<(ord(cur[i])-ord('a'))
    bit_arr.append(bb)
b=0
res=0
def go(idx,cnt,bit):
    if cnt==M:
        global res
        c=0
        for cur in bit_arr:
            if cur == (cur & bit):
                c+=1
        res=max(res,c)
        return
    for i in range(idx,26):
        if not bit & (1<<i):
            go(i+1,cnt+1,bit|(1<<i))

for cur in "antic":
    b |= 1<<(ord(cur)-ord('a'))

M-=5
if M>=0:
    go(0,0,b)
print(res)








