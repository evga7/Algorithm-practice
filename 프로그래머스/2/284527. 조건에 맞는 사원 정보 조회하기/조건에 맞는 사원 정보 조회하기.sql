-- 코드를 작성해주세요
select sum(c.SCORE) SCORE,c.EMP_NO,b.EMP_NAME,b.POSITION,b.EMAIL from HR_DEPARTMENT a join HR_EMPLOYEES b on a.DEPT_ID=b.DEPT_ID join HR_GRADE c on b.EMP_NO=c.EMP_NO
where c.YEAR ='2022'
group by c.EMP_NO
order by SCORE desc limit 1