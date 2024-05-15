def solution(s):
    answer = 0
    m={')':'(','}':'{',']':'['}
    for i in range(len(s)):
        t=s[i:]+s[:i]
        st=[]
        f=1
        for cur in t:
            if cur==')' or cur==']' or cur=='}':
                if st and st[-1]==m[cur]:
                    st.pop()
                    continue
                else:
                    f=0
                    break
            else:
                st.append(cur)
        if not st and f:
            answer+=1
    return answer