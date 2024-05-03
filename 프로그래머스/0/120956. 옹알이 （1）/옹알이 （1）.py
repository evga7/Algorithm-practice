st=set()
def solution(babbling):
    answer = 0
    st.add('aya')
    st.add('ye')
    st.add('woo')
    st.add('ma')
    answer = 0
    for x in babbling:
        for cur in st:
            x=x.replace(cur,' ')
        x=x.replace(' ','')
        if not x:
            answer+=1
    return answer