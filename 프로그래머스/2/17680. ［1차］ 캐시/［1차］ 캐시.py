from collections import *
def solution(cacheSize, cities):
    answer = 0
    v=deque()
    for cur in cities:
        cur=cur.lower()
        if cur in v:
            del v[v.index(cur)]
            answer+=1
        else:
            if len(v)==cacheSize and v:
                v.popleft()
            answer+=5
        if cacheSize:
            v.append(cur)
    return answer