from collections import *
def solution(numbers):
    answer = []
    numbers.sort()
    l=len(numbers)
    st=set()
    for i in range(l):
        for j in range(i+1,l):
            st.add(numbers[i]+numbers[j])
    return sorted(list(st))