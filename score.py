#!/bin/env python

import sys

annotation_path = sys.argv[1]
model_path = sys.argv[2]
score_path = sys.argv[3]

import pandas
import pickle
import xgboost

model = pickle.load(open(model_path, 'rb'))
model_features = model.__dict__['feature_names']
df = pandas.read_csv(annotation_path, sep="\t", index_col=0)
for f in model_features:
    if not f in df.columns:
        df[f] = 0
df = df[model_features]
dat_dmatrix = xgboost.DMatrix(df)
model_predict = model.predict(dat_dmatrix)
score = pandas.DataFrame({'rsid': df.index.tolist(), 'score': model_predict})
score = score[['rsid', 'score']]
score.to_csv(score_path, sep="\t", index=False)

