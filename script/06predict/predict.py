#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pandas
import pickle
import xgboost

def main(args):
    args_instance = args.instance
    args_libsvm = args.libsvm
    args_model_bst = args.model_bst
    args_output = args.output
    #
    instance = pandas.read_csv(args_instance, header=None)
    dtest = xgboost.DMatrix(args_libsvm)
    bst = xgboost.Booster()
    bst.load_model(args_model_bst)
    preds = bst.predict(dtest)
    #
    pred_df = pandas.DataFrame({"instance": instance[0].tolist(), "probability": preds.tolist()})
    pred_df['chrom'], pred_df['start_end'] = pred_df['instance'].str.split(':', 1).str
    pred_df['start'], pred_df['end'] = pred_df['start_end'].str.split('-', 1).str
    pred_df['start'] = pandas.to_numeric(pred_df['start']) - 1
    pred_df['end'] = pandas.to_numeric(pred_df['end'])
    pred_df['probability'] = pandas.to_numeric(pred_df['probability'])
    pred_df = pred_df[['chrom', 'start', 'end', 'probability']]
    pred_df.to_csv(args_output, sep = "\t", header = False, index = False, float_format='%.4f')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--instance', dest='instance', type=str)
    parser.add_argument('--libsvm', dest='libsvm', type=str)
    parser.add_argument('--model_bst', dest='model_bst', type=str, help="Save the booster model to a file")
    parser.add_argument('-o', dest='output', type=str)
    args = parser.parse_args()
    main(args)


