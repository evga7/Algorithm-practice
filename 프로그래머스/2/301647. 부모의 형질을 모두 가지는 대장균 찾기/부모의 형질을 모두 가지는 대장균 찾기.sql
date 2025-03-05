-- 코드를 작성해주세요
select a.ID,a.GENOTYPE,b.GENOTYPE PARENT_GENOTYPE from ECOLI_DATA a inner join ECOLI_DATA b on a.PARENT_ID=b.id
where (b.GENOTYPE & a.GENOTYPE) = b.GENOTYPE
order by a.id