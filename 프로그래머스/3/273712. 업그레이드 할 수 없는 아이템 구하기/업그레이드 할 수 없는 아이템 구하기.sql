-- 코드를 작성해주세요
select ITEM_ID ,ITEM_NAME,RARITY from ITEM_INFO
where ITEM_ID not in 
(select PARENT_ITEM_ID from ITEM_TREE where PARENT_ITEM_ID is not null)
order by iTEM_ID desc