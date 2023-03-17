#!/opt/conda/envs/dsenv/bin/python

import sys, os
import logging
from joblib import load
import pandas as pd

numeric_features = ["if"+str(i) for i in range(1,14)]
categorical_features = ["cf"+str(i) for i in range(1,27)] + ["day_number"]

fields = ["id", "label"] + numeric_features + categorical_features
fields_without_category = ["id", "label"] + numeric_features

sys.path.append('.')

#
# Init the logger
#
logging.basicConfig(level=logging.DEBUG)
logging.info("CURRENT_DIR {}".format(os.getcwd()))
logging.info("SCRIPT CALLED AS {}".format(sys.argv[0]))
logging.info("ARGS {}".format(sys.argv[1:]))

#load the model
model = load("1.joblib")

#fields = """doc_id,hotel_name,hotel_url,street,city,state,country,zip,class,price,
#num_reviews,CLEANLINESS,ROOM,SERVICE,LOCATION,VALUE,COMFORT,overall_ratingsource""".replace("\n",'').split(",")

#read and infere
read_opts=dict(
        sep=',', names=fields, index_col=False, header=None,
        iterator=True, chunksize=100
)

for df in pd.read_csv(sys.stdin, **read_opts):
    df = df[fields_without_category]
    df.if13 = df.if13.str[:-2].replace('', 0).astype(int)
#     logging.info(f'?????????????????????????????len(df) = {len(df)} df:{df}')
    pred = model.predict_proba(df)[::,1]

#     logging.info(f'len(df) = {len(df)},len(pred) = {len(pred)} df:{df},pred:{pred}')
    out = zip(df.id, pred)
    print("\n".join(["{0},{1}".format(*i) for i in out]))

