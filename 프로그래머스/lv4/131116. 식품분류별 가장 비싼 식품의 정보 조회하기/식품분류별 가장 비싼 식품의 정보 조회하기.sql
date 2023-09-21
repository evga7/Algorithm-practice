SELECT CATEGORY,price MAX_PRICE,PRODUCT_NAME from FOOD_PRODUCT 
where price in (select max(price) from food_product group by category) and 
CATEGORY in ('과자','국','식용유','김치')
group by CATEGORY
order by MAX_PRICE desc