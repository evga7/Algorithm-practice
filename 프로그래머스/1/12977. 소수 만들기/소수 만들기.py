from collections import *
import math
def solution(nums):
    v=set(range(2,3001))
    answer=0
    for i in range(2,int(math.sqrt(3000))+1):
        if i in v:
            v-=set(range(i*i,3001,i))
    l=len(nums)
    m=defaultdict(int)
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if nums[i]+nums[j]+nums[k] in v:
                    answer+=1
    return answer