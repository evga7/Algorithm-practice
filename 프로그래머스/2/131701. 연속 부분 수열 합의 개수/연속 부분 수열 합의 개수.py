def solution(elements):
    answer = 0
    st=set()
    l=len(elements)
    for i in range(l):
        t=elements[i:]+elements[:i]
        s=0
        for cur in t:
            s+=cur
            st.add(s)
        
    return len(st)