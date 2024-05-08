def solution(cards1, cards2, goal):
    answer = ''
    idx,idx2=0,0
    l,l2=len(cards1),len(cards2)
    i=0
    while (idx<l or idx2<l2) and i<len(goal):
        if idx<l and goal[i]==cards1[idx]:
            idx+=1
        if idx2<l2 and goal[i]==cards2[idx2]:
            idx2+=1
        i+=1
    return "Yes" if (idx+idx2)==len(goal) else "No"