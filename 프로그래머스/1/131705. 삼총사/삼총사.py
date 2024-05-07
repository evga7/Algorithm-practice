from collections import *
def solution(number):
    answer = 0
    m=defaultdict(int)
    l=len(number)
    for i in range(l):
        for j in range(i+1,l):
            if -(number[i]+number[j]) in m:
                answer+=m[-(number[i]+number[j])]
        m[number[i]]+=1

            
            
    return answer