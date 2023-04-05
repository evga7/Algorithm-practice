def solution(cookie):
    answer = 0
    for i in range(len(cookie)-1,-1,-1):
        st = set()
        s=0
        for j in range(i,len(cookie)):
            s+=cookie[j]
            st.add(s)
        js=0
        for j in range(i-1,-1,-1):
            js += cookie[j]
            if js in st:
                answer=max(js,answer)
            
    return answer