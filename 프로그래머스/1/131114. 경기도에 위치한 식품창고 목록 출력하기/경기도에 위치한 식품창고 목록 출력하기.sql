-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME,ADDRESS,if (FREEZER_YN is NULL,'N',FREEZER_YN) FREEZER_YN from food_warehouse
where address like '경기도%'
order by warehouse_id