-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME,ADDRESS,if(FREEZER_YN is null ,'N' ,FREEZER_YN) from FOOD_WAREHOUSE
where address like '%경기도%'
order by WAREHOUSE_ID