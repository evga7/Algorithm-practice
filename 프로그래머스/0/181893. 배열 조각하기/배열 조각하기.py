def solution(arr, query):
    op=0
    for cur in query:
        if op:
            arr=arr[cur:]
        else:
            arr=arr[:cur+1]
        op=1-op
    return arr