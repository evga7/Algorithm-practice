from collections import *
def solution(s):
    answer = []
    for cur in s:
        q=deque()
        zcnt=0
        cnt=0
        for i in range(len(cur)):
            if len(q)>1 and cur[i]=='0' and q[-2]=='1'and q[-1]=='1':
                q.pop()
                q.pop()
                cnt+=1
                continue
            if cur[i]=='0':
                zcnt+=1
            q.append(cur[i])
        s=""
        while q:
            if not zcnt:
                s+="110"*cnt
                cnt=0
            if q[0]=='0':
                zcnt-=1
            s+=q.popleft()
        if cnt:
            s+="110"*cnt
        answer.append(s)
    return answer