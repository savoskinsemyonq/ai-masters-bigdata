drop table if exists hw2_pred;
create TABLE IF NOT EXISTS hw2_pred (id INT, label FLOAT) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES('seporatorChar'='\t', 'quoteChar'='\"') STORED AS TEXTFILE 
location 'savoskinsemyonq_hw2_pred'
TBLPROPERTIES ("skip.header.line.count"="1");