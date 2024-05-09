def solution(board, moves):
    answer = 0
    n,m=len(board),len(board[0])
    s=[[] for _ in range(m)]
    st=[]
    for i in range(m):
        for j in range(n-1,-1,-1):
            if board[j][i]:
                s[i].append(board[j][i])
            else:
                break
    for cur in moves:
        if s[cur-1]:
            p=s[cur-1].pop()
            if st and st[-1]==p:
                st.pop()
                answer+=1
            else:
                st.append(p)
    return answer*2