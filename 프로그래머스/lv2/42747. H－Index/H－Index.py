import bisect
def solution(citations):
    citations.sort()
    N=len(citations)
    left=0
    right=10000
    while left<=right:
        mid=left+right>>1
        a=bisect.bisect_left(citations,mid)
        if N-a>=mid and a<=mid:
            left=mid+1
        else:
            right=mid-1
    return left-1