import heapq
def solution(A, B):
    answer = 0
    idx=0
    q=[]
    A.sort(reverse=True)
    B.sort(reverse=True)
    for cur in A:
        while idx<len(B) and B[idx]>cur:
            heapq.heappush(q,B[idx])
            idx+=1
        if q and q[0]>cur:
            answer+=1
            heapq.heappop(q)
    return answer