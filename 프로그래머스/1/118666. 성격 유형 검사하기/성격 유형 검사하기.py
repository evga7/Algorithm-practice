from collections import *
m=defaultdict(int)
p=[0,3,2,1,0,1,2,3]
def solution(survey, choices):
    answer = ''
    temp='RTCFJMAN'
    for cur in temp:
        m[cur]=0
    for i in range(len(survey)):
        l,r,c=survey[i][0],survey[i][1],choices[i]
        if 1<=c<=3:
            m[l]+=p[c]
        elif 5<=c<=7:
            m[r]+=p[c]
    v=[]
    for cur in m.keys():
        v.append((m[cur],cur))
    v.sort(key=lambda x:(-x[0],x[1]))
    for i in range(0,len(temp),2):
        x,y=temp[i],temp[i+1]
        if m[x]>=m[y]:
            answer+=x
        else:
            answer+=y
    return answer