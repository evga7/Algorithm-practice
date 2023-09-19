-- 코드를 입력하세요
SELECT PRODUCT_ID,PRODUCT_NAME,PRODUCT_CD,CATEGORY,price from FOOD_PRODUCT
group by price
order by price desc limit 1