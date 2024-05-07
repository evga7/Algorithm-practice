def solution(absolutes, signs):
    l=len(signs)
    answer=0
    for i in range(l):
        num,op=absolutes[i],signs[i]
        if op==False:
            num*=-1
        answer+=num
    return answer