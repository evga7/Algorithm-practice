def solution(s):
    answer = []
    s=s.lstrip('{').rstrip('}').split('},{')
    v=[]
    for cur in s:
        v.append(list(map(int,cur.split(','))))
    v.sort(key=lambda x:len(x))
    st=set()
    for cur in v:
        for x in cur:
            if x in st:continue
            answer.append(x)
            st.add(x)
    return answer