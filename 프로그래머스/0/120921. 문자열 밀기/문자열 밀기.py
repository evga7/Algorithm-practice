from collections import *
def solution(A, B):
    answer = 987654321
    q2=deque(A)
    cnt=0
    while cnt<=len(A):
        if ''.join(q2)==B:
            answer=min(answer,cnt)
        q2.appendleft(q2.pop())
        cnt+=1
    if answer==987654321:
        answer=-1
    return answer