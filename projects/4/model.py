#!/opt/conda/envs/dsenv/bin/python

from pyspark.sql.types import *
from pyspark.ml.feature import *
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline


tokenizer = Tokenizer(inputCol="reviewText", outputCol="text")
hasher = HashingTF(numFeatures=100, binary=True, inputCol=tokenizer.getOutputCol(), outputCol="word_vector")
assembler = VectorAssembler(inputCols=[hasher.getOutputCol(), "comment_length", "vote"], outputCol="features")
lr = LogisticRegression(labelCol="overall", maxIter=25)

pipeline = Pipeline(stages=[
    tokenizer,
    hasher,
    assembler,
    lr
])