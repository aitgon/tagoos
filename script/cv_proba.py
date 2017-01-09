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

train_libsvm_temp_path = tempfile.NamedTemporaryFile().name
test_libsvm_temp_path = tempfile.NamedTemporaryFile().name

outdir_path = "."



#def main_bak(argv):
#    # I/O paths
#    libsvm_path = sys.argv[1] #pandas.read_csv("annotation.libsvm", sep="\t", header=None)
#    instance_path = os.path.join(dirname(libsvm_path), "instance.txt")
#    variable_path = os.path.join(dirname(libsvm_path), "variable.txt")
#    #instance = sys.argv[2] #pandas.read_csv("instance.txt", sep="\t", header=None)
#    #variable = sys.argv[3] #pandas.read_csv("variable.txt", sep="\t", header=None)
#    rsid2chrom_path = sys.argv[2] #pandas.read_csv("rsid2chrom.tsv", sep="\t", header=None, index_col=0)
#    #
#    cv_proba_pkl_path = sys.argv[3] #cv_proba_path.pkl"
#    outdir_path = dirname(cv_proba_pkl_path)
#    #
#    # load data
#    libsvm = pandas.read_csv(libsvm_path, sep="\t", header=None)
#    instance = pandas.read_csv(instance_path, sep="\t", header=None)
#    variable = pandas.read_csv(variable_path, sep="\t", header=None)
#    rsid2chrom = pandas.read_csv(rsid2chrom_path, sep="\t", header=None, index_col=0)
#    #
#    # loop over chromosomes
#    chrom_list = sorted(rsid2chrom[1].unique())
#    for chr in chrom_list:
#    # write cv_probas to pkl
#    pickle.dump(cv_probas, open(cv_proba_pkl_path, "wb"))

def worker(chr, cv_probas, libsvm, rsid2chrom, instance):
    print(chr)
    chr_int = int(chr[3:])
    cv_probas[chr_int] = {}
    #
    cv_path = os.path.join(outdir_path, "CV", "%d"%chr_int)
    test_libsvm_path = os.path.join(cv_path, "test.libsvm")
    test_instance_path = os.path.join(cv_path, "test_instance.txt")
    train_libsvm_path = os.path.join(cv_path, "train.libsvm")
    train_instance_path = os.path.join(cv_path, "train_instance.txt")
    #
    try:
        os.makedirs(cv_path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    test_libsvm = libsvm.loc[(rsid2chrom[1]==chr).tolist(),]
    test_instance = instance.loc[(rsid2chrom[1]==chr).tolist()]
    test_libsvm.to_csv(test_libsvm_path, index=None, header=None)
    test_instance.to_csv(test_instance_path, index=None, header=None)
    train_libsvm = libsvm.loc[(rsid2chrom[1]!=chr).tolist(),]
    train_instance = instance.loc[(rsid2chrom[1]!=chr).tolist()]
    train_libsvm.to_csv(train_libsvm_path, index=None, header=None)
    train_instance.to_csv(train_instance_path, index=None, header=None)
    xdm_train = xgboost.DMatrix(train_libsvm_path)
    model = xgboost.train({'silent': True}, xdm_train)
    y_proba = model.predict(xgboost.DMatrix(test_libsvm_path))
    #
    y_test_proba=pandas.DataFrame({'label': test_instance[0].tolist(), 'proba': y_proba}, index=test_instance[0])
    y_test_proba.sort_values(by=['proba', 'label'], axis=0, ascending=[False, False], inplace=True)
    y_test_proba.to_csv(os.path.join(cv_path, 'y_test_proba.tsv'), sep="\t", index=False, index_label="variant")
    #
    #cv_probas[chr_int]['test_libsvm_path'] = test_libsvm_path
    #cv_probas[chr_int]['y_proba'] = y_proba
    return chr_int, {'test_libsvm_path' : test_libsvm_path, 'y_proba' : y_proba}

from functools import partial
from itertools import repeat
from multiprocessing import Pool, freeze_support

def main(argv):
    # I/O paths
    nproc = int(sys.argv[1]) # number of parallel procs
    libsvm_path = sys.argv[2] #pandas.read_csv("annotation.libsvm", sep="\t", header=None)
    instance_path = os.path.join(dirname(libsvm_path), "instance.txt")
    variable_path = os.path.join(dirname(libsvm_path), "variable.txt")
    #instance = sys.argv[2] #pandas.read_csv("instance.txt", sep="\t", header=None)
    #variable = sys.argv[3] #pandas.read_csv("variable.txt", sep="\t", header=None)
    rsid2chrom_path = sys.argv[3] #pandas.read_csv("rsid2chrom.tsv", sep="\t", header=None, index_col=0)
    cv_proba_pkl_path = sys.argv[4] #cv_proba_path.pkl"
    outdir_path = dirname(cv_proba_pkl_path)
    #
    # load data
    libsvm = pandas.read_csv(libsvm_path, sep="\t", header=None)
    instance = pandas.read_csv(instance_path, sep="\t", header=None)
    variable = pandas.read_csv(variable_path, sep="\t", header=None)
    rsid2chrom = pandas.read_csv(rsid2chrom_path, sep="\t", header=None, index_col=0)
    #
    # loop over chromosomes
    chrom_list = sorted(rsid2chrom[1].unique())
    #manager = Manager() # create only 1 mgr
    #d = manager.dict() # create only 1 dict
    cv_probas = {}
    #number_processes = 3
    #pool = multiprocessing.Pool(number_processes)
    #results = pool.map_async(work, tasks)
    #for chr in chrom_list:
    #    #chr_int = int(chr[3:])
    #    chr_int, y_proba,test_libsvm_path = worker(chr, cv_probas, libsvm, rsid2chrom, instance)
    #    cv_probas[chr_int]['test_libsvm_path'] = test_libsvm_path
    #    cv_probas[chr_int]['y_proba'] = y_proba
    with Pool(nproc) as pool:
        a_args = chrom_list
        #worker(chr, cv_probas, libsvm, rsid2chrom, instance)
        cv_probas = dict(pool.map(partial(worker, cv_probas=cv_probas, libsvm=libsvm, rsid2chrom=rsid2chrom, instance=instance), a_args))
    # write cv_probas to pkl
    #print(cv_probas)
    pickle.dump(cv_probas, open(cv_proba_pkl_path, "wb"))

if __name__ == "__main__":
    main(sys.argv[1:])

