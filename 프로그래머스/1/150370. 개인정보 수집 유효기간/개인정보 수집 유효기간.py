from collections import *
import datetime
def cal(today,before):
    y,m,d=list(map(int,today.split('.')))
    y2,m2,d2=list(map(int,before.split('.')))
    y,m=y*28*12,m*28
    y2,m2=y2*28*12,m2*28
    return (y+m+d)-(y2+m2+d2)
    
def solution(today, terms, privacies):
    answer = []
    m=defaultdict(int)
    for x in terms:
        a,b=x.split()
        m[a]=int(b)*28
    for i,cur in enumerate(privacies):
        y,op=cur.split()
        if cal(today,y)>=m[op]:
            answer.append(i+1)
        
    return answer