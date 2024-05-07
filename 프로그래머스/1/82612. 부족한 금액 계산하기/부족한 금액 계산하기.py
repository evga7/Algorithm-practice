def solution(price, money, count):
    r=count*(count+1)//2 *price
    return r-money if r>money else 0