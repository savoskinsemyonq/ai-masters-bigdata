add file fill.py;
add file projects/2/model.py;
add file projects/2/predict.py;
insert into table hw2_pred
select transform(*) using 'predict.py' as (pred, id)
from (select * from hw2_test
where hw2_test.if1 > 20 and hw2_test.if1 < 40) as q;