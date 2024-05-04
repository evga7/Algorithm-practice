def solution(common):
    answer = 0
    s=common[1]-common[0]
    l=len(common)
    for i in range(2,l):
        if common[i]-common[i-1]!=s:
            s=-987654321
            break
    if s!=-987654321:
        return common[l-1]+s
    return common[l-1]*(common[1]//common[0])