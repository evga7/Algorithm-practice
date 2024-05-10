-- 코드를 입력하세요
SELECT a.PRODUCT_CODE,sum(a.price*b.SALES_AMOUNT) SALES
from product a join OFFLINE_SALE b on a.PRODUCT_ID=b.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc,PRODUCT_CODE

