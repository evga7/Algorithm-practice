a=[[0 for _ in range(101)] for _ in range(101)]
def solution(n, results):
    answer = 0
    for cur in results:
        x,y=cur[0],cur[1]
        a[x][y]=1
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if a[i][k] and a[k][j]:
                    a[i][j]=1
    for i in range(n+1):
        cnt=0
        for j in range(n+1):
            if a[i][j] or a[j][i]:cnt+=1
        if cnt==n-1:
            answer+=1
    return answer