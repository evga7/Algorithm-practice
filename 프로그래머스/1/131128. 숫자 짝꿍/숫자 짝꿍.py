from collections import *
def solution(X, Y):
    answer = ''
    c,c2=Counter(X),Counter(Y)
    for i in range(9,-1,-1):
        s=str(i)
        z=min(c[s],c2[s])
        answer+=str(i)*z
    if not answer:
        answer="-1"
    if answer[0]=="0":
        answer="0"
    return answer