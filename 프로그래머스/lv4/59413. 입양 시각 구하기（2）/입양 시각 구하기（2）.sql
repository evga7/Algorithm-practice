SET @HOUR:=-1;
SELECT (@HOUR := @HOUR +1) HOUR,
(select count(hour(DATETIME)) from animal_outs 
                           where hour(DATETIME)=@HOUR) count
from ANIMAL_OUTS
where @HOUR<23
order by @HOUR
