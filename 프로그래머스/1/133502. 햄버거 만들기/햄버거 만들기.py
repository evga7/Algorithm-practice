def solution(ingredient):
    answer = 0
    st=""
    for cur in ingredient:
        st+=str(cur)
        if len(st)>=4 and st[-4:]=="1231":
            answer+=1
            st=st[:-4]
    return answer