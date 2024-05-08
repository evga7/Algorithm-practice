import math
p=[0 for _ in range(1000001)]
def c():
    for i in range(2,int(math.sqrt(1000000))+1):
        if p[i]:continue
        for j in range(i*i,1000001,i):
            p[j]=1
            
        
def solution(n):
    answer = 0
    c()
    for i in range(2,n+1):
        if not p[i]:
            answer+=1
    return answer