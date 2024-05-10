-- 코드를 작성해주세요
select sum(b.score) SCORE,a.eMP_NO,a.EMP_NAME,a.POSITION,a.EMAIL from HR_EMPLOYEES a join HR_GRADE b on a.emp_no=b.emp_no
where b.year='2022'
group by a.emp_no
order by score desc limit 1