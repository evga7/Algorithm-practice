
SELECT concat("/home/grep/src/",a.BOARD_ID,'/',a.FILE_ID,a.FILE_NAME,a.FILE_EXT) FILE_PATH from USED_GOODS_FILE a 
join USED_GOODS_BOARD b on a.BOARD_ID=b.BOARD_ID
where views = (select max(views) from USED_GOODS_BOARD )
order by FILE_ID desc