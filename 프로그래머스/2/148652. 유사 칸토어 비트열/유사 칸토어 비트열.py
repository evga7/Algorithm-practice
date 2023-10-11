def go(n,pos):
    if n==1:
        if pos<=2:
            return pos
        else:
            return pos-1
    div=5**(n-1)
    o_cnt=4**(n-1)
    idx=(pos-1)//div
    if idx<2:
        return o_cnt*idx+go(n-1,pos-(idx*div))
    elif idx==2:
        return o_cnt*idx
    else:
        return o_cnt*(idx-1)+go(n-1,pos-(idx*div))
    
def solution(n, l, r):
    return go(n,r)-go(n,l-1)