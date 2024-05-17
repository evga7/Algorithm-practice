def solution(s):
    answer = []
    v=[]
    t=""
    temp=[]
    for cur in s:
        if cur.isdigit():
            t+=cur
        elif cur==',':
            if t:
                temp.append(int(t))
                t=""
        elif cur=='}':
            if t:
                temp.append(int(t))
                t=""
            if temp:
                v.append(temp)
                temp=[]
    v.sort(key=lambda x:len(x))
    st=set()
    for cur in v:
        for x in cur:
            if x in st:continue
            answer.append(x)
            st.add(x)
    return answer