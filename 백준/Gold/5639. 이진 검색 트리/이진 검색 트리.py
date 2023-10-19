import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
INF=sys.maxsize
a=[]
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BT:
    def __init__(self,head):
        self.head=head
    def insert(self,node):
        cur=self.head
        while cur!=None:
            if cur.val<node.val:
                if cur.right==None:
                    cur.right=node
                    break
                cur=cur.right
            else:
                if cur.left==None:
                    cur.left=node
                    break
                cur=cur.left
while True:
    try:
        a.append(int(input()))
    except:
        break
    
h=BT(Node(a[0]))    
for i in range(1,len(a)):
    h.insert(Node(a[i]))
def p(cur):
    if cur==None:
        return
    if cur.left!=None:
        p(cur.left)
    if cur.right!=None:
        p(cur.right)
    print(cur.val)
    
p(h.head)
    
    