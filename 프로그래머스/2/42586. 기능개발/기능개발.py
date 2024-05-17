import heapq
def solution(progresses, speeds):
    answer = []
    i=0
    l=len(speeds)
    while i<l:
        x,y=progresses[i],speeds[i]
        cnt=(100-x+(y-1))//y
        c=1
        while i+1<l:
            x,y=progresses[i+1],speeds[i+1]
            cnt2=(100-x+(y-1))//y
            if cnt>=cnt2:
                c+=1
                i+=1
            else:
                break
        i+=1
        answer.append(c)
    return answer