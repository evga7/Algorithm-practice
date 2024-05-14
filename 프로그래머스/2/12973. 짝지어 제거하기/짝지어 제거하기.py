def solution(s):
    answer=1
    st=[]
    for cur in s:
        if st and st[-1]==cur:
            while st and st[-1]==cur:
                st.pop()
        else:
            st.append(cur)
    if st:
        answer=0
    return answer