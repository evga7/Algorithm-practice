import sys
def input(): return sys.stdin.readline().rstrip()
S=input()
f=0
res=""
ff=0
if S[0].isupper():
    ff=1
elif S.find('_')>=0:
    for i in range(len(S)):
        cur=S[i]
        if cur.isupper():
            ff = 1
            break
        if cur=='_':
            if i==0 or i==(len(S)-1):
                ff=1
                break
            f+=1
            continue
        if f:
            if f>1:
                ff=1
                break
            res+=cur.upper()
            f=0
        else:
            res+=cur
else:
    for cur in S:
        if cur.isupper():
            res+='_'+cur.lower()
            continue
        else:
            res+=cur
if ff:
    print("Error!")
else:
    print(res)