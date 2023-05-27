import sys
import math
from collections import *
def input():return sys.stdin.readline().rstrip()
N=int(input())
def chk(num):
    for i in range(2,int(math.sqrt(num))+1):
        if not num%i:
            return False
    return True
def go(idx,s):
    if idx==N:
        print(s)
        return
    for i in range(1,10):
        if chk(s*10+i):
            go(idx+1,s*10+i)
for i in range(2,10):
    if chk(i):
        go(1,i)