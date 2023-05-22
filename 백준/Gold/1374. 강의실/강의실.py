from collections import *
import heapq
import sys
def input():return sys.stdin.readline().rstrip()
N=int(input())
m=defaultdict(int)
st=set()
for i in range(N):
    q,s,e=map(int,input().split())
    m[s]+=1
    m[e]-=1
    st.add(s)
    st.add(e)
cnt=0
res=0
for cur in sorted(list(st)):
    cnt+=m[cur]
    res=max(res,cnt)
print(res)