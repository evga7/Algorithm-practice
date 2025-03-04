-- 코드를 입력하세요
SELECT hour(datetime) HOUR , count(*) COUNT from ANIMAL_OUTS
group by HOUR
having HOUR>=9 and HOUR<20
order by HOUR