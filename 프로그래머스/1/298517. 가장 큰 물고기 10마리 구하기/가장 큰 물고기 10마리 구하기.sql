-- 코드를 작성해주세요
select ID,ifnull(LENGTH,10) LENGTH from FISH_INFO
order by length desc,id limit 10