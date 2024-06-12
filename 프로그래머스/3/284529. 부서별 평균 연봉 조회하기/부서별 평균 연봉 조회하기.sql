-- 코드를 작성해주세요
select a.dept_id,a.DEPT_NAME_EN,round(avg(b.sal)) avg_sal from HR_DEPARTMENT a join HR_EMPLOYEES b on a.dept_id=b.dept_id
group by a.dept_id,a.DEPT_NAME_EN
order by avg_sal desc