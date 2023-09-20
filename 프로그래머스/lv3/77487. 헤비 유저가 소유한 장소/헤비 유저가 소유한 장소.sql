-- 코드를 입력하세요
SELECT ID,NAME,HOST_ID from PLACES
where HOST_ID in (select HOST_ID from places group by host_id having count(host_id)>=2)
order by id