import sys
def input():return sys.stdin.readline().rstrip()
while True:
    s=input()
    if s=='end':
        break
    x_cnt=s.count('X')
    o_cnt=s.count('O')
    if o_cnt>x_cnt or x_cnt>o_cnt+1:
        print("invalid")
        continue
    else:
        a=[]
        a.append(s[:3])
        a.append(s[3:6])
        a.append(s[6:9])
        x_win=0
        o_win=0
        for i,cur in enumerate(a):
            if list(zip(*a))[i].count('X')==3:
                x_win=1
            if list(zip(*a))[i].count('O') == 3:
                o_win = 1
            if cur.count('X')==3:
                x_win=1
            if cur.count('O')==3:
                o_win=1
        if s[0]==s[4]==s[8]=='X':
            x_win=1
        if s[0]==s[4]==s[8]=='O':
            o_win=1
        if s[2] == s[4] == s[6] == 'X':
            x_win = 1
        if s[2] == s[4] == s[6] == 'O':
            o_win = 1
        if o_win and x_win:
            print("invalid")
            continue
        elif x_win:
            if x_cnt==o_cnt+1:
                print("valid")
                continue
        elif o_win:
            if x_cnt==o_cnt:
                print("valid")
                continue
        else:
            if x_cnt==5 and o_cnt==4:
                print("valid")
                continue
    print("invalid")