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
sys.setrecursionlimit(10 ** 5)
dp = [[-1 for _ in range(10001)]for _ in range(4)]
dx = [0, 1, 0, -1]  # 오 아래 왼 위
dy = [1, 0, -1, 0]
T=int(si().rstrip())
st=set()
def go(op,idx,s):
    if idx==0:
        return 1
    if dp[op][idx]!=-1:
        return dp[op][idx]
    ret=0
    for i in range(op,4):
        if idx-i>=0:
            ret+=go(i,idx-i,s+str(i))
    dp[op][idx]=ret
    return dp[op][idx]

for i in range(T):
    N=int(si().rstrip())
    print(go(1,N,""))









