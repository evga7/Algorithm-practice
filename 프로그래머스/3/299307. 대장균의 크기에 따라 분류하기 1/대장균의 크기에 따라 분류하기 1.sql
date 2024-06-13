-- 코드를 작성해주세요
select a.id,case when a.SIZE_OF_COLONY<=100 then 'LOW' when a.SIZE_OF_COLONY>100 and a.SIZE_OF_COLONY<=1000 then 'MEDIUM' when a.SIZE_OF_COLONY>1000 then 'HIGH' end size from ECOLI_DATA a
order by a.id