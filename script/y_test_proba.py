#!/bin/env python

#dat_bak = pandas.read_hdf(dat_path, 'key') # reads data
#cv_splitted_data = cv_split_data(dat, outdir_path) # splits data in dic with chrom keys
#cv_probas = cv_proba(cv_splitted_data, outdir_path) # writes dict with cv_probas[chrom]['y_proba'] = y_proba
#roc_plot(cv_probas, roc_path, auc_path) # plots roc
#precision_recall_plot(cv_probas, precision_recall_path, auprc_path) # plots precision recall   

from os.path import dirname
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score

import errno
import numpy
import os
import pandas
import pickle
import sys
import tempfile
import xgboost

#libsvm = pandas.read_csv("annotation.libsvm", sep="\t", header=None)
#instance = pandas.read_csv("instance.txt", sep="\t", header=None)
#variable = pandas.read_csv("variable.txt", sep="\t", header=None)
#rsid2chrom = pandas.read_csv("rsid2chrom.tsv", sep="\t", header=None, index_col=0)
#rsid2chrom = rsid2chrom.loc[instance[0],]

from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support

def main(argv):
    test_libsvm_path = sys.argv[1] #os.path.join(cv_path, "test.libsvm")
    test_instance_path = sys.argv[2] #os.path.join(cv_path, "test_instance.txt")
    train_libsvm_path = sys.argv[3] #os.path.join(cv_path, "train.libsvm")
    y_test_proba_tsv = sys.argv[4] # output
    #
    outdir = os.path.dirname(y_test_proba_tsv)
    auc_path = os.path.join(outdir, "auc.txt")
    #
    test_instance = pandas.read_csv(test_instance_path, header=None)
    xdm_train = xgboost.DMatrix(train_libsvm_path)
    xdm_test = xgboost.DMatrix(test_libsvm_path)
    #################
    scale_pos_weight = (xdm_train.get_label()==-1).sum()/(xdm_train.get_label()==1).sum()
    pars = {'silent': True, 'scale_pos_weight': scale_pos_weight, 'max_delta_step' : 1}
    model = xgboost.train(pars, xdm_train)
    y_test_proba = model.predict(xdm_test)
    #
    y_test_label = xdm_test.get_label().tolist()
    y_test_label=[int(label) for label in y_test_label] # to integer
    #
    y_test_proba = pandas.DataFrame({'label': y_test_label, 'proba': y_test_proba}, index=test_instance[0])
    y_test_proba.sort_index(inplace=True)
    y_test_proba.sort_values(by=['proba', 'label'], axis=0, ascending=[False, False], inplace=True)
    y_test_proba.to_csv(y_test_proba_tsv, sep="\t", index=True, index_label="variant")
    fpr, tpr, thresholds = roc_curve(y_test_proba['label'].tolist(), y_test_proba['proba'].tolist(), pos_label=1)
    roc_auc = auc(fpr, tpr)
    roc_auc = "%.2f" % roc_auc
    with open(auc_path, 'w') as fout:
        fout.write(roc_auc)


if __name__ == "__main__":
    main(sys.argv[1:])

