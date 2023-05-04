from collections import *
import sys
def input():return sys.stdin.readline().rstrip()
S=input()
st=set()
q=deque()
q.append((S,S,len(S)-1))
res=0
while q:
    cur,sts,cost=q.popleft()
    if cost==0:
        st.add(sts)
        res+=1
        continue
    for nxt in [cur[1:],cur[:len(cur)-1]]:
        nxt_sts=sts+' '+nxt
        if nxt and not nxt_sts in st:
            q.append((nxt,nxt_sts,cost-1))
            st.add(nxt_sts)
print(res)