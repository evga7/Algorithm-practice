from collections import *
import sys
def input(): return sys.stdin.readline().rstrip()
N=int(input())
for i in range(N):
    s1,s2=input().split()
    a,b=Counter(s1),Counter(s2)
    if a==b:
        print(s1+' & '+s2+' are anagrams.')
    else:
        print(s1 + ' & ' + s2 + ' are NOT anagrams.')