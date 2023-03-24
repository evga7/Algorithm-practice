def solution(s):
    answer = True
    st=[]
    for cur in s:
        if cur==')':
            if not st:
                return False
            st.pop()
            continue
        st.append(cur)
    return not st