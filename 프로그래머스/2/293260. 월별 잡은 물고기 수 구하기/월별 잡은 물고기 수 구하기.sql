-- 코드를 작성해주세요
select count(*) fish_count,MONTH(TIME) MONTH from fish_info
group by MONTH
having fish_count>0
order by MONTH