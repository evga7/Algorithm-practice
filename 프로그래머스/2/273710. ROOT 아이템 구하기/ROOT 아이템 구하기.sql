-- 코드를 작성해주세요
select a.ITEM_ID,a.ITEM_NAME from item_info a join item_tree b on a.item_id=b.item_id
where b.PARENT_ITEM_ID is NULL
order by a.item_id