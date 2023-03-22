def solution(n):
    answer = 0
    left=1
    right=1
    s=0
    while right<=n+1:
        if s>=n:
            if s==n:
                answer+=1
            s-=left
            left+=1
        else:
            s+=right
            right+=1
    return answer