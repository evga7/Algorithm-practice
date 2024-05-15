def solution(n, words):
    answer = []
    st=set()
    r=words[0][0]
    cnt=0
    for i,cur in enumerate(words):
        if cur in st:
            break
        if r==cur[0]:
            st.add(cur)
        else:
            break
        r=cur[len(cur)-1]
        cnt+=1
    if cnt==len(words):
        return [0,0]
    return [cnt%n+1,cnt//n+1]