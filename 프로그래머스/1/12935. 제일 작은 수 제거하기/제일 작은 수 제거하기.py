def solution(arr):
    m=min(arr)
    del arr[arr.index(m)]
    if not arr:
        arr.append(-1)
    return arr