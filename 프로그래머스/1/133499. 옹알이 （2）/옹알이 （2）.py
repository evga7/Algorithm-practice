
def solution(babbling):
    st={'aya','ye','woo','ma'}
    st2={'ayaaya','yeye','woowoo','mama'}
    answer = 0
    for cur in babbling:
        f=1
        for x in st2:
            if x in cur:
                f=0
                break
        if not f:continue
        temp=cur
        for x in st:
            temp=temp.replace(x,' ')
        temp=temp.replace(' ','')
        if not temp:
            answer+=1
    return answer