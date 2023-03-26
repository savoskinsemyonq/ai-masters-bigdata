#!/opt/conda/envs/dsenv/bin/python
import pandas as pd
print(1+1)
numeric_features = ["if"+str(i) for i in range(1,14)]
categorical_features = ["cf"+str(i) for i in range(1,27)] + ["day_number"]

fields = ["id", "label"] + numeric_features + categorical_features
fields_without_category = ["id", "label"] + numeric_features

read_table_opts = dict(sep="\t",names=['id','score'],index_col=False)
y_true = pd.read_table('/home/users/datasets/criteo/criteo_valid_large_filtered_labels', **read_table_opts)
read_table_opts1 = dict(sep="\t",names=['id','score'],index_col=False)
y_pred= pd.read_table('http://name1:9870/webhdfs/v1/user/savoskinsemyonq/pred_with_filter/part-00000?op=OPEN', **read_table_opts1)
read_table_opts2 = dict(sep="\t",names=fields_without_category, index_col=False)
df = pd.read_table('http://name1:9870/webhdfs/v1/datasets/criteo/criteo_valid_large_features/part-00000?op=OPEN', **read_table_opts2)
read_table_opts3 = dict(sep="\t",names=fields_without_category, index_col=False)
df_train = pd.read_table('/home/users/datasets/criteo/criteo_train500', **read_table_opts3)
print(df_train.head(30))

y_true = y_true.sort_values(by='id')
y_pred = y_pred.sort_values(by='id')
df = df.sort_values(by='id')
print(df.head(30))
print(y_pred[y_pred.id>75779264])
print(y_true[y_true.id>75779264])
print(f"df = {len(df)}, len(y_pred) = {len(y_true)}, len(y_true) = {len(y_true)}")