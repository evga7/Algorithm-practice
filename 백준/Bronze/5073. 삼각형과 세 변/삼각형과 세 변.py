from collections import *
import sys
def input():return sys.stdin.readline().rstrip()

while True:
    a=list(map(int,input().split()))
    if not a[0] and not a[1] and not a[2]:
        break
    a.sort()
    res=""
    m=defaultdict(int)
    for cur in a:
        m[cur]+=1
    if a[0]+a[1]<=a[2]:
        res="Invalid"
    elif len(m)==1:
        res="Equilateral"
    elif len(m)==2:
        res="Isosceles"
    elif len(m)==3:
        res="Scalene"
    print(res)
