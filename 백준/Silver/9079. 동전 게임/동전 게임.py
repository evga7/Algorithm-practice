import sys
import heapq
def input(): return sys.stdin.readline().rstrip()
T=int(input())

op=[448,56,7,292,146,73,273,84]
def go(s):
    q=[]
    q.append((0,int(s,2)))
    st=set()
    while q:
        cost,x=heapq.heappop(q)
        if x==511 or x==0:
            return cost
        for i in range(8):
            nxt=x^op[i]
            if not nxt in st:
                st.add(nxt)
                q.append((cost+1,nxt))
    return -1

while T:
    T-=1
    a=[list(input().split()) for _ in range(3)]
    s=''
    for i in range(3):
        for j in range(3):
            cur=a[i][j]
            if cur=='H':
                s+='1'
            else:
                s+='0'
    print(go(s))