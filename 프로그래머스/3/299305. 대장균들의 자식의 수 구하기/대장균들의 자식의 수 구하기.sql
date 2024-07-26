-- 코드를 작성해주세요
select a.id ID ,COALESCE(b.child_count, 0) CHILD_COUNT from ecoli_data a left join 
(select parent_id,count(*) child_count from ecoli_data
group by parent_id
having parent_id is not NULL) b on a.id=b.parent_id
order by ID