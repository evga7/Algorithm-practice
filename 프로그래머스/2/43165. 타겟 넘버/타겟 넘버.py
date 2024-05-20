res=0
def go(idx,s,l,t,nu):
    if idx==l:
        global res
        if s==t:
            res+=1
        return
    go(idx+1,s-nu[idx],l,t,nu)
    go(idx+1,s+nu[idx],l,t,nu)
def solution(numbers, target):
    answer = 0
    go(0,0,len(numbers),target,numbers)
    return res