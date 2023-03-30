def solution(a):
    answer=len(a)
    st=[]
    for cur in a:
        while st and cur<st[-1]:
            st.pop()
            if st:
                answer-=1
        st.append(cur)
    return answer