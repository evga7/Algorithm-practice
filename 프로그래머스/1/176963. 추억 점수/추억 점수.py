from collections import *
def solution(name, yearning, photo):
    m=defaultdict(int)
    answer=[]
    for i in range(len(name)):
        m[name[i]]=yearning[i]
    for x in photo:
        r=0
        for cur in x:
            if cur in m:
                r+=m[cur]
        answer.append(r)
    return answer