-- 코드를 작성해주세요
select concat(ceil(month(DIFFERENTIATION_DATE)/3),'Q') QUARTER,count(*) ECOLI_COUNT from ECOLI_DATA
group by QUARTER
order by QUARTER