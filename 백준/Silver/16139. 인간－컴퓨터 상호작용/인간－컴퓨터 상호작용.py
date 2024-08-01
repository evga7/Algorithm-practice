from collections import *
import bisect
# sys.setrecursionlimit(100000)
import sys
def input(): return sys.stdin.readline().rstrip()
MAX = sys.maxsize
MOD = int(1e9) + 9
s=input()
m=[[0 for _ in range(26)] for _ in range(len(s)+1)]
M=int(input())
m2=defaultdict(int)
for i in range(1,len(s)+1):
    cur=s[i-1]
    cur_num=ord(cur)-ord('a')
    m[i][cur_num]=m[i-1][cur_num]+1
    for j in range(26):
        if cur_num==j:continue
        m[i][j]=m[i-1][j]
for i in range(M):
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    cur_num=ord(a)-ord('a')
    print(m[c+1][cur_num]-m[b][cur_num])