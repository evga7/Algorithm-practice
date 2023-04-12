import sys
def input():return sys.stdin.readline().rstrip()
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev
    def insert(self,data):
        c=Node(data)
        pp=self.prev
        if pp!=None:
            pp.next=c
            c.prev=pp
        c.next=self
        self.prev=c

    def delete(self):
        p=self.prev
        if p!=None:
            self.prev=p.prev
            if p.prev!=None:
                self.prev.next=self
            del p

head=Node('')
s=input()
N=int(input())
p=head
for cur in s:
    p.data=cur
    p.next=Node('')
    p.next.prev=p
    p=p.next

for i in range(N):
    a=list(input().split())
    if a[0]=='L':
        if not p.prev==None:
            p=p.prev
    elif a[0]=='D':
        if not p.next==None:
            p=p.next
    elif a[0]=='B':
        p.delete()
    elif a[0]=='P':
        p.insert(a[1])

while p.prev!=None:
    p=p.prev
while p:
    print(p.data,end='')
    p=p.next