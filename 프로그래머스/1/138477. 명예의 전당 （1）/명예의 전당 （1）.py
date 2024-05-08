import heapq
def solution(k, score):
    q=[]
    answer=[]
    for cur in score:
        q.append(cur)
        q.sort(reverse=True)
        if len(q)<k:
            answer.append(q[-1])
        else:
            answer.append(q[k-1])
            
    return answer