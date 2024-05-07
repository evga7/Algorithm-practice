def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        cur=arr[i]
        if not stk:
            stk.append(cur)
            i+=1
        else:
            if stk[-1]<cur:
                stk.append(cur)
                i+=1
            else:
                stk.pop()
    return stk