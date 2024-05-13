-- 코드를 작성해주세요
select a.ID,a.GENOTYPE,b.GENOTYPE PARENT_GENOTYPE from ECOLI_DATA a inner join ECOLI_DATA b on b.id=a.parent_id
where a.GENOTYPE & b.GENOTYPE = b.GENOTYPE
order by a.id