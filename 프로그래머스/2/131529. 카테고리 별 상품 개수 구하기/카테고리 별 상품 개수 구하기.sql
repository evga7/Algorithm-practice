-- 코드를 입력하세요
SELECT left(PRODUCT_CODE,2) CATEGORY,count(PRODUCT_CODE) from product
group by CATEGORY
order by CATEGORY