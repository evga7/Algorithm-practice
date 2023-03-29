def solution(n, times):
    answer = 0
    left=0
    right=int(1e19)
    while left<=right:
        mid=left+right>>1
        c=0
        for cur in times:
            c+=mid//cur
        if c>=n:
            right=mid-1
        else:
            left=mid+1
    return left