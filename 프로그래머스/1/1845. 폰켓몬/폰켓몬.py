from collections import *
def solution(nums):
    answer = 0
    l=len(nums)//2
    c=Counter(nums)
    return min(l,len(c.keys()))