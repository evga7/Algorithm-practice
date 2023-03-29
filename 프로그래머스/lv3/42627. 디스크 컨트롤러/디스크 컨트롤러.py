import heapq
def solution(jobs):
    answer = 0
    jobs.sort()
    idx=0
    end=0
    cnt=0
    q=[]
    while cnt<len(jobs):
        while idx<len(jobs) and jobs[idx][0]<=end:
            heapq.heappush(q,(jobs[idx][1],jobs[idx][0]))
            idx+=1
        if q:
            c=heapq.heappop(q)
            end+=c[0]
            answer+=end-c[1]
            cnt+=1
        else:
            end+=1
    return answer//len(jobs)