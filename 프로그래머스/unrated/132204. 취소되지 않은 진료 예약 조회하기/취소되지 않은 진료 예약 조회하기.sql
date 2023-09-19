-- 코드를 입력하세요
SELECT c.APNT_NO,a.PT_NAME,a.PT_NO,b.MCDP_CD,b.DR_NAME,c.APNT_YMD from PATIENT a join APPOINTMENT c on a.PT_NO=c.PT_NO 
join DOCTOR b on b.DR_ID=c.MDDR_ID
where c.APNT_CNCL_YN ='N' and APNT_YMD like '%2022-04-13%' and c.MCDP_CD='CS'
order by c.APNT_YMD