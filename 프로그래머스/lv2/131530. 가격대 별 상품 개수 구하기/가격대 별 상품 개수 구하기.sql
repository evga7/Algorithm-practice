-- 코드를 입력하세요
SELECT if (price>=10000 and price<20000,10000,truncate(price,-4)) PRICE_GROUP,count(PRODUCT_ID) PRODUCTS from product
group by  PRICE_GROUP
order by PRICE_GROUP