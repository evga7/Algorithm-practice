-- 코드를 입력하세요
SELECT MCDP_CD 진료과코드,count(MCDP_CD) 5월예약건수 from appointment
where APNT_YMD like '2022-05%'
group by MCDP_CD
order by 5월예약건수,진료과코드