-- 코드를 작성해주세요
select a.ID,b.FISH_NAME,a.LENGTH LENGTH from FISH_INFO a join FISH_NAME_INFO b on a.FISH_TYPE=b.FISH_TYPE
where (a.FISH_TYPE,a.LENGTH) in (select FISH_TYPE,max(length) from fish_info group by FISH_TYPE)
order by a.id