from collections import *
def solution(a):
    m=defaultdict(list)
    answer=0
    for i in range(len(a)):
        m[a[i]].append(i)
    for c in m:
        cnt=0
        back=-1
        for cur in m[c]:
            left=max(0,cur-1)
            right=min(cur+1,len(a)-1)
            if back!=left and a[left]!=c:
                cnt+=1
            elif a[right]!=c:
                back=right
                cnt+=1
        answer=max(answer,cnt)

    return answer*2