def solution(score):
    answer = []
    v=[]
    l=len(score)
    v2=[0 for _ in range(l)]
    for i,cur in enumerate(score):
        v.append((cur[0]+cur[1],i))
    v.sort(reverse=True)
    idx=1
    cnt=0
    for i in range(l):
        q,w=v[i][0],v[i][1]
        v2[w]=idx
        if i+1<l and v[i][0]==v[i+1][0]:
            cnt+=1
            continue
        else:
            idx+=cnt
            cnt=0
        idx+=1+cnt
    return v2[:l]