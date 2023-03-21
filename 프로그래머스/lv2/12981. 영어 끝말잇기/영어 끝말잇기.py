def solution(n, words):
    answer = []
    s=''
    st=set()
    for i,cur in enumerate(words):
        if s and s!=cur[0] or cur in st:
            return [(i%n) +1,i//n +1]
        st.add(cur)
        s=cur[-1]
    return [0,0]