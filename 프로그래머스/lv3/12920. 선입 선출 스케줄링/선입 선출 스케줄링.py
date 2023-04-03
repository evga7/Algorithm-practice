def solution(n, cores):
    if len(cores)>=n:
        return n
    n-=len(cores)
    left=1
    right=int(1e13)
    while left<=right:
        mid=left+right>>1
        cnt=0
        for cur in cores:
            cnt+=mid//cur
        if cnt>=n:
            right=mid-1
        else:
            left=mid+1
    right+=1
    for cur in cores:
        n-=(right-1)//cur
    for i,cur in enumerate(cores):
        if not right%cur:
            n-=1
        if not n:
            return i+1

    return -1