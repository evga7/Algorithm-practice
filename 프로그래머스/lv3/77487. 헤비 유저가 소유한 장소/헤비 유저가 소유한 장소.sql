-- 코드를 입력하세요
select id ,name ,host_id from places
where HOST_ID in (select host_id from places group by host_id having count(*)>1)
order by id
    