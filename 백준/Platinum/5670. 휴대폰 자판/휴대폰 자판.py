import sys
from collections import *
dx = [0,-1,0,1]  # 오 위 왼 아
dy = [1,0,-1,0]
def is_inside(x,y,N,M):
    return 0<x<=N and 0<y<=M
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
class Node:
    def __init__(self,key):
        self.key=key
        self.child={}
        self.count=0

class Trie:
    def __init__(self):
        self.head=Node(None)

    def insert(self,s):
        cur=self.head
        for c in s:
            if not c in cur.child:
                cur.child[c]=Node(c)
            cur=cur.child[c]
            cur.count+=1
        cur.child['last']=True
def go(f,cur):
    global cnt
    if len(cur.child)>1 or not f:
        for c in cur.child:
            if c!='last':
                cnt+=cur.child[c].count
    for c in cur.child:
        if c!='last':
            go(f+1,cur.child[c])
def find_click(l, cur):
    global cnt

    if len(cur.child) > 1 or l == 0:
        for c in cur.child:
            if c != '*':
                cnt += cur.child[c].count
    for c in cur.child:
        if c != '*':
            find_click(l+1, cur.child[c])

while True:
    N=input()
    if not N:
        exit(0)
    cnt=0
    N=int(N)
    a=[input() for _ in range(N)]
    trie=Trie()
    for cur in a:
        trie.insert(cur)
    go(0,trie.head)
    print("{:.2f}".format(round((cnt/N),2)))