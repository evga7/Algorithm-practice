from collections import *
import sys
# sys.setrecursionlimit(100000)
def input(): return sys.stdin.readline().rstrip()
#
INF = sys.maxsize
N=int(input())
l=defaultdict(int)
h=defaultdict(int)
m_len=0
for i in range(N):
    s=input()
    m_len=max(m_len,len(s))
    l[s]+=1
for i in range(N):
    s=input()
    h[s]+=1
    m_len = max(m_len, len(s))
M=int(input())
def go(s):
    l_cnt=0
    h_cnt=0
    for i in range(len(s)):
        ss=""
        for j in range(i,len(s)):
            ss+=s[j]
            if m_len<len(ss):break
            if ss in l:
                l_cnt += l[ss]
            if ss in h:
                h_cnt+=h[ss]
    sub=abs(l_cnt-h_cnt)
    if l_cnt<h_cnt:
        print("LOW %d"%sub)
    elif l_cnt>h_cnt:
        print("HIGH %d"%sub)
    else:
        print("GOOD")



for i in range(M):
    s=input()
    go(s)

