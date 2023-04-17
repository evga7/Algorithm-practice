import heapq
import sys
def input():return sys.stdin.readline().rstrip()
s=input()
s2=input()
st=set()
q=[]
heapq.heappush(q,(0,s2))
res=0
while q:
    cost,cur=heapq.heappop(q)
    if cur==s:
        res=1
        break
    if cur[-1]=='A':
        nxt=cur[:len(cur)-1]
        if not nxt in st and len(nxt)>=len(s):
            st.add(nxt)
            heapq.heappush(q,(cost+1,nxt))
    if cur[0]=='B':
        nxt=cur[1:]
        nxt=nxt[::-1]
        if not nxt in st and len(nxt)>=len(s):
            st.add(nxt)
            heapq.heappush(q,(cost+1,nxt))

print(res)