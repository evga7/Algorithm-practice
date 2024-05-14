def solution(s):
    answer = True
    st=[]
    for cur in s:
        if cur==')':
            if st and st[-1]=='(':
                st.pop()
            else:
                return False
        else:
            st.append('(')
    if not st:
        return True
    return False