def solution(arr):
    answer = 0
    while True:
        t=[0 for _ in range(len(arr))]
        for i,cur in enumerate(arr):
            nxt=cur
            if cur>=50 and not cur&1:
                nxt=cur//2+1
            elif cur<50 and cur&1:
                nxt=cur*2+1
            t[i]=nxt
        if arr==t:
            break
        answer+=1
        arr=t[:]
    return answer