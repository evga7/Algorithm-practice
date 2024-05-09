def solution(s):
    answer = 0
    cnt=0
    cnt2=0
    x=""
    for cur in s:
        if not cnt:
            x=cur
        if x!=cur:
            cnt2+=1
        else:
            cnt+=1
        if x!=cur and cnt==cnt2:
            answer+=1
            cnt=0
            cnt2=0
    return answer+1 if cnt else answer