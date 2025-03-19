-- 코드를 작성해주세요
select count(*) FISH_COUNT,max(ifnull(length,10)) MAX_LENGTH,FISH_TYPE from FISH_INFO 
group by FISH_TYPE
having avg(ifnull(length,10))>=33
order by FISH_TYPE