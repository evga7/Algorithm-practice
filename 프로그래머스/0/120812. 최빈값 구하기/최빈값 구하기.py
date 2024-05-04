from collections import *
def solution(array):
    c=Counter(array)
    a=[]
    for cur in c.keys():
        a.append((c[cur],cur))
    a.sort(reverse=True)
    if len(a)>1:
        if a[0][0]==a[1][0]:
            return -1
    return a[0][1]