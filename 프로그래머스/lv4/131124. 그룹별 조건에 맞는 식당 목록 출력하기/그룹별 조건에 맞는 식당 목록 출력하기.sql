

SELECT a.MEMBER_NAME,b.REVIEW_TEXT,date_format(b.REVIEW_DATE,'%Y-%m-%d') REVIEW_DATE from MEMBER_PROFILE a 
join REST_REVIEW b on a.MEMBER_ID=b.MEMBER_ID
where a.member_id = (select member_id c from REST_REVIEW group by member_id order by count(member_id) desc limit 1)
order by REVIEW_DATE,REVIEW_TEXT


