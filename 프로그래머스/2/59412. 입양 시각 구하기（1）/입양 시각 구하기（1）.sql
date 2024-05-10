-- 코드를 입력하세요
SELECT HOUR(datetime) HOUR,count(*) from animal_outs
where HOUR(datetime)>=09 and HOUR(datetime)<20
group by HOUR
order by HOUR