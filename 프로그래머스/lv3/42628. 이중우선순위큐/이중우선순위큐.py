import heapq
def solution(operations):
    answer = []
    min_q=[]
    max_q=[]
    l=0
    for cur in operations:
        s=cur.split()
        op=s[0]
        num=int(s[1])
        if op=='I':
            heapq.heappush(min_q,num)
            heapq.heappush(max_q,-num)
            l+=1
        elif op=='D':
            if l:
                if num==1:
                    heapq.heappop(max_q)
                else:
                    heapq.heappop(min_q)
                l-=1
            if not l:
                min_q.clear()
                max_q.clear()
    a=0
    b=0
    if min_q:
        b=heapq.heappop(min_q)
    if max_q:
        a=heapq.heappop(max_q)
    return [-a,b]