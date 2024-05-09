v=[]
def solution(s, skip, index):
    answer = ''
    st=set()
    t=set(skip)
    for i in range(26):
        c=chr(ord('a')+i)
        if not c in t:
            st.add(c)
    for i in range(26):
        c=chr(ord('a')+i)
        if c in st:
            v.append(c)
    for cur in s:
        nxt=(v.index(cur)+index)%len(v)
        answer+=v[nxt]
    return answer