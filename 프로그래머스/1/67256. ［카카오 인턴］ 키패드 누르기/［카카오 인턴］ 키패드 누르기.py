from collections import *
m=defaultdict(str)
def cal(x,y,x2,y2):
    return abs(x-x2)+abs(y-y2)
def solution(numbers, hand):
    answer = ''
    pos=[[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    l,r=[3,0],[3,2]
    for i in [1,4,7]:
        m[i]='L'
    for i in [3,6,9]:
        m[i]='R'
    if hand=="right":
        hand=1
    else:
        hand=0
    for cur in numbers:
        if cur in m:
            c=m[cur]
            answer+=c
            if c=='L':
                l=pos[cur]
            else:
                r=pos[cur]
        else:
            p=pos[cur]
            c1,c2=cal(l[0],l[1],p[0],p[1]),cal(r[0],r[1],p[0],p[1])
            ccc=hand
            if c1<c2:
                ccc=0
            elif c1>c2:
                ccc=1
            if ccc:
                r=pos[cur]
                answer+='R'
            else:
                l=pos[cur]
                answer+='L'
                    
    return answer