#dat_bak = pandas.read_hdf(dat_path, 'key') # reads data
#cv_splitted_data = cv_split_data(dat, outdir_path) # splits data in dic with chrom keys
#cv_probas = cv_proba(cv_splitted_data, outdir_path) # writes dict with cv_probas[chrom]['y_test_proba'] = y_test_proba
#roc_plot(cv_probas, roc_path, auc_path) # plots roc
#precision_recall_plot(cv_probas, precision_recall_path, auprc_path) # plots precision recall   

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
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

def precision_recall_plot(y_test_proba_path_list, precision_recall_path, auprc_path):
    recalls = []
    precisions = []
    precision2s = []
    auprcs = []
    base_recall = numpy.linspace(1, 0, 101)
    fig, ax = pyplot.subplots()
    cv_rocs = {}
    #for chrom in sorted(cv_probas.keys()):
    for i,y_test_proba_path in enumerate(y_test_proba_path_list):
        #if not cv_probas[chrom] is None:
        #y_test_proba_path = cv_probas[chrom]['y_test_proba']
        y_test_proba_df = pandas.read_csv(y_test_proba_path, sep="\t", header=0)
        y_test_label = y_test_proba_df.label.tolist()
        y_test_proba = y_test_proba_df.proba.tolist()
        #
        precision, recall, thresholds = precision_recall_curve(y_test_label, y_test_proba, pos_label=1)
        auprc = average_precision_score(y_test_label, y_test_proba)
        recalls.append(recall)
        auprcs.append(auprc)
        precision2 = (numpy.interp(base_recall[::-1], recall[::-1], precision[::-1]))[::-1]
        precisions.append(precision)
        precision2s.append(precision2)
        ax.plot(recall, precision, 'b', alpha=0.05)
    precision2s = numpy.array(precision2s)
    mean_precision2s = precision2s.mean(axis=0)
    auprc_mean = "%.2f" % numpy.array(auprcs).mean()
    with open(auprc_path, 'w') as fout:
        fout.write(auprc_mean)
    ax.plot(base_recall, mean_precision2s, 'b', label="auprc: %s" % (auprc_mean))
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.legend(loc="lower right")
    fig.savefig(precision_recall_path)

def main(argv):
    y_test_proba_path_list = sys.argv[1:-1]
    precision_recall_path = sys.argv[-1] #"roc.png"
    auprc_path = os.path.join(os.path.dirname(precision_recall_path), 'auprc.txt') #"auc.txt"
    #cv_probas = pickle.load(open(cv_proba_pkl_path, 'rb'))
    precision_recall_plot(y_test_proba_path_list, precision_recall_path, auprc_path)

if __name__ == "__main__":
    main(sys.argv[1:])

