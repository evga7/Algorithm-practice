-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) YEAR,(b.m-a.SIZE_OF_COLONY) YEAR_DEV,ID from ECOLI_DATA a join (select year(DIFFERENTIATION_DATE) year,max(SIZE_OF_COLONY) m from ecoli_data group by year )  b on year(a.DIFFERENTIATION_DATE)=b.year
order by YEAR,YEAR_DEV
