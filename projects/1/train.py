#!/opt/conda/envs/dsenv/bin/python

import os, sys
import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import dump

#
# Import model definition
#
from model import model

numeric_features = ["if"+str(i) for i in range(1,13)]
categorical_features = ["cf"+str(i) for i in range(1,27)] + ["day_number"]

fields = ["id", "label"] + numeric_features + categorical_features
fields_without_category = ["id", "label"] + numeric_features

#
# Logging initialization
#
logging.basicConfig(level=logging.DEBUG)
logging.info("CURRENT_DIR {}".format(os.getcwd()))
logging.info("SCRIPT CALLED AS {}".format(sys.argv[0]))
logging.info("ARGS {}".format(sys.argv[1:]))

#
# Read script arguments
#
try:
  proj_id = sys.argv[1] 
  train_path = sys.argv[2]
except:
  logging.critical("Need to pass both project_id and train dataset path")
  sys.exit(1)


logging.info(f"TRAIN_ID {proj_id}")
logging.info(f"TRAIN_PATH {train_path}")

#
# Read dataset
#
#fields = """doc_id,hotel_name,hotel_url,street,city,state,country,zip,class,price,
#num_reviews,CLEANLINESS,ROOM,SERVICE,LOCATION,VALUE,COMFORT,overall_ratingsource""".replace("\n",'').split(",")

read_table_opts = dict(sep="\t", names=fields_without_category,index_col=False)
df = pd.read_table(train_path, **read_table_opts)

df = df[fields_without_category]
#split train/test
X_train, X_test, y_train, y_test = train_test_split(
    df.drop(columns=["label"]), df.label, test_size=0.33, random_state=42
)

#
# Train the model
#
logging.info(f"fields: {len(df)}")
# print(df.head(5))
# print(df.if1.isna().sum())
model.fit(X_train, y_train)

model_score = model.score(X_test, y_test)

logging.info(f"model score: {model_score:.3f},fields: {len(df)}")

# save the model
dump(model, "1.joblib")


