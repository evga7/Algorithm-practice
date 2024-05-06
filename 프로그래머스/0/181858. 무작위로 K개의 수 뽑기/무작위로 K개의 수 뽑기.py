from collections import *
st=set()
def solution(arr, k):
    answer = []
    for cur in arr:
        if len(answer)>=k:break
        if not cur in st:
            st.add(cur)
            answer.append(cur)
    while len(answer)<k:
        answer.append(-1)
    return answer