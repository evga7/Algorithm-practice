def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt=1
        j=1
        while j<i:
            if not i%j:
                cnt+=1
            j+=1
        if cnt&1:
            answer-=i
        else:
            answer+=i
    return answer