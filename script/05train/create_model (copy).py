#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pandas
import pickle
import xgboost
from sklearn.model_selection import LeaveOneGroupOut

def main(args):

    args_libsvm = args.libsvm
    args_feature = args.feature
    args_feature_importance = args.feature_importance
    args_chrom = args.chrom
    args_cv_pkl = args.cv_pkl
    args_model_pkl = args.model_pkl
    args_nthread = args.nthread
    #
    # Features
    feature_name_df = pandas.read_csv(args_feature, sep="\t", names=['feature_id', 'feature_name'])
    feature_names = feature_name_df.feature_name.tolist()
    #
    # Load dmatrix
    dtrain = xgboost.DMatrix(args_libsvm, feature_names=['label'] + feature_names)
    #
    # Params
    scale_pos_weight = (dtrain.get_label()==0).sum()/(dtrain.get_label()==1).sum()
    #
    # Params
    params = {
        'objective': 'binary:logistic',  # choose logistic regression loss function for binary classification
        'max_delta_step' : 1,
        'eval_metric': 'auc',
        'scale_pos_weight': scale_pos_weight,
        'silent': 1,
        'nthread': args_nthread,
        'seed' : 42,
        # optimized
        'max_depth': 11,
        'min_child_weight': 7,
        'subsample': 1,
        'colsample_bytree': 1,
        'eta':0.2,
        #
        'num_boost_round': 11,
        }
    #
    # CV
    groups = pandas.read_csv(args_chrom, header=None)[0]
    folds = LeaveOneGroupOut()
    folds.get_n_splits(X=dtrain, y=dtrain.get_label(), groups=groups)
    cv = xgboost.cv(params=params, dtrain=dtrain, folds=folds, num_boost_round=999, early_stopping_rounds=10)
    pickle.dump(cv, open(args_cv_pkl, "wb"))
    #
    # Model
    model = xgboost.train(params, dtrain, num_boost_round=params['num_boost_round'])
    pickle.dump(model, open(args_model_pkl, "wb"))
    #
    # Feature importance
    feature_importance = pandas.DataFrame.from_records(list(model.get_score(importance_type="gain").items()))
    feature_importance.columns = ['feature', 'weight']
    feature_importance = feature_importance.loc[:, ['feature', 'weight']]
    feature_importance.sort_values(by='weight', ascending=False, inplace=True)
    feature_importance.to_csv(args_feature_importance, sep="\t", index=False, header=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--libsvm', dest='libsvm', type=str)
    parser.add_argument('--feature', dest='feature', type=str)
    parser.add_argument('--chrom', dest='chrom', type=str)
    parser.add_argument('--cv_pkl', dest='cv_pkl', type=str)
    parser.add_argument('--model_pkl', dest='model_pkl', type=str)
    parser.add_argument('--feature_importance', dest='feature_importance', type=str)
    parser.add_argument('--nthread', dest='nthread', type=int)
    args = parser.parse_args()
    main(args)
    

