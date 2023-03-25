import heapq
def solution(n, works):
    answer = 0
    w=[]
    for cur in works:
        w.append(-cur)
    heapq.heapify(w)
    while n and w:
        a=heapq.heappop(w)+1
        if a:
            heapq.heappush(w,a)
        n -= 1
    for cur in w:
        answer+=cur*cur
    return answer