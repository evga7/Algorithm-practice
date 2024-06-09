SELECT a.REST_ID,a.REST_NAME,a.FOOD_TYPE,a.FAVORITES,a.ADDRESS,round(avg(b.REVIEW_SCORE),2) SCORE 
from REST_INFO a join REST_REVIEW b on a.REST_ID=b.REST_ID
where a.address like '서울%'
group by REST_ID
order by SCORE desc,a.FAVORITES desc