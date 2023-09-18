-- 코드를 입력하세요
SELECT concat('/home/grep/src/',b.BOARD_ID,+'/',b.FILE_ID,b.FILE_NAME,b.FILE_EXT) FILE_PATH
from USED_GOODS_BOARD a join USED_GOODS_FILE b on a.BOARD_ID=b.BOARD_ID
where views in (select max(views) from USED_GOODS_BOARD)
order by b.FILE_id desc