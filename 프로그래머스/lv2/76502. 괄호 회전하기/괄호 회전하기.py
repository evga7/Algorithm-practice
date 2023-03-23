def chk(ss):
    st=[]
    for cur in ss:
        if cur=='[' or cur=='(' or cur=='{':
            st.append(cur)
        else:
            if not st:
                return 0
            if cur==']' and st[-1]=='[':
                st.pop()
            elif cur==')' and st[-1]=='(':
                st.pop()
            elif cur=='}' and st[-1]=='{':
                st.pop()
    return not st
def solution(s):
    answer = 0
    for i in range(len(s)):
        ss=s[i:]+s[:i]
        if chk(ss):
            answer+=1
    return answer