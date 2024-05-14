
def solution(n):
    left=1
    right=2
    s=3
    answer = 1
    while left<right and right<n:
        if s>=n:
            if s==n:
                answer+=1
            s-=left
            left+=1
        else:
            right+=1
            s+=right
    return answer