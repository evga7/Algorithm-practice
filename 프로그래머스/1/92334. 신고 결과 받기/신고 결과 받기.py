from collections import *
def solution(id_list, report, k):
    m=defaultdict(int)
    m2=defaultdict(int)
    answer = [0 for _ in range(len(id_list))]
    st=set()
    report=list(set(report))
    for i,cur in enumerate(id_list):
        m2[cur]=i
    for cur in report:
        x,y=cur.split()
        m[y]+=1
        if m[y]>=k:
            st.add(y)
    for cur in report:
        x,y=cur.split()
        if y in st:
            answer[m2[x]]+=1
    return answer