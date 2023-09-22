-- 코드를 입력하세요
SELECT distinct(a.cart_id) from CART_PRODUCTS a ,CART_PRODUCTS b
where a.CART_ID=b.CART_ID and a.name ='Milk' and b.name='Yogurt'
order by a.cart_id