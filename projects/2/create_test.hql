drop table if exists hw2_test;
create TEMPORARY EXTERNAL TABLE IF NOT EXISTS hw2_test (id INT, label INT,
if1 INT,if2 INT,if3 INT,if4 INT,if5 INT,if6 INT,if7 INT,if8 INT,if9 INT,if10 INT,if11 INT,if12 INT) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
WITH SERDEPROPERTIES('seporatorChar'='\t', 'quoteChar'='\"') STORED AS TEXTFILE
location '/datasets/criteo/criteo_test_large_features'
TBLPROPERTIES ("skip.header.line.count"="1") ;
-- !hdfs dfs -cp /datasets/criteo/criteo_test_large_features /user/savoskinsemyonq/my_hive_db/hw2_test