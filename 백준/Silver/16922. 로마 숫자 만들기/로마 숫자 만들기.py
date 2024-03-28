import sys
def input():
    return sys.stdin.readline().rstrip()
m=[set() for _ in range(21)]
a=[1,5,10,50]
def go(idx,s):
    if s in m[idx]:
        return
    m[idx].add(s)
    if idx==N:
        return
    for i in range(4):
        go(idx+1,s+a[i])
N=int(input())
go(0,0)
print(len(m[N]))
