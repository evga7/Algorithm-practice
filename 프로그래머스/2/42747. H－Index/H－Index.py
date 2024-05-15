def solution(citations):
    answer = 0
    left=0
    right=10000
    while left<=right:
        mid=left+right>>1
        c=0
        for cur in citations:
            if cur>=mid:
                c+=1
        if c<mid:
            right=mid-1
        else:
            left=mid+1
    return left-1