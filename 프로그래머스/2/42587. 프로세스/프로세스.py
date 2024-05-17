import heapq
from collections import *
def solution(priorities, location):
    answer = 0
    dq=deque()
    q=[]
    for i,cur in enumerate(priorities):
        dq.append((cur,i))
        heapq.heappush(q,(-cur))
    
    while dq:
        while q and -q[0]!=dq[0][0]:
            dq.append(dq.popleft())
        if dq[0][1]==location:
            return answer+1
        heapq.heappop(q)
        dq.popleft()
        answer+=1
            