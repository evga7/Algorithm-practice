select a.ITEM_ID,a.ITEM_NAME,a.RARITY from ITEM_INFO a inner join item_tree b on a.item_id=b.item_id
where b.PARENT_ITEM_ID in (select item_id from item_info where rarity='RARE')
order by a.item_id desc