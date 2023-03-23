al="ZYXWVUTSRQPONMLKJIHGFEDCBAABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solution(name):
    answer = 0
    N=len(name)
    pos=N-1
    for i,cur in enumerate(name):
        j=i+1
        while j<N and name[j]=='A':
            j+=1
        answer += min(26 - al[:26].index(cur) - 1, 26 - al[26:].index(cur))
        pos=min(pos,i+N-j+min(i,N-j))
    return answer+pos