def solution(common):
    answer = 0
    s=common[1]-common[0]
    m=-987654321
    if common[0]!=0:
        m=common[1]//common[0]
    l=len(common)
    for i in range(2,l):
        if common[i]-common[i-1]!=s:
            s=-987654321
        if common[i-1]==0:continue
        if common[i]//common[i-1]!=m:
            m=-987654321
    if s!=-987654321:
        return common[l-1]+s
    if m!=-987654321:
        return common[l-1]*m
    return answer