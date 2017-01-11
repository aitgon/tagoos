#dat_bak = pandas.read_hdf(dat_path, 'key') # reads data
#cv_splitted_data = cv_split_data(dat, outdir_path) # splits data in dic with chrom keys
#cv_probas = cv_proba(cv_splitted_data, outdir_path) # writes dict with cv_probas[chrom]['y_proba'] = y_proba
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

def roc_plot(cv_probas, roc_path, auc_path):
    fprs = []
    tprs = []
    tpr2s = []
    aucs = []
    base_fpr = numpy.linspace(0, 1, 101)
    fig, ax = pyplot.subplots()
    cv_rocs = {}
    for chrom in sorted(cv_probas.keys()):
        if not cv_probas[chrom] is None:
            y_test_proba_path = cv_probas[chrom]['y_test_proba']
            y_test_proba_df = pandas.read_csv(y_test_proba_path, sep="\t", header=0)
            y_test_label = y_test_proba_df.label.tolist()
            y_test_proba = y_test_proba_df.proba.tolist()
            #
            fpr, tpr, thresholds = roc_curve(y_test_label, y_test_proba, pos_label=1)
            roc_auc = auc(fpr, tpr)
            fprs.append(fpr)
            tpr2 = numpy.interp(base_fpr, fpr, tpr)
            tprs.append(tpr)
            tpr2s.append(tpr2)
            aucs.append(roc_auc)
            cv_rocs[chrom] = {'fpr': fpr, 'tpr': tpr, 'thresholds': thresholds}
            ax.plot(fpr, tpr, 'b', alpha=0.05)
    tpr2s = numpy.array(tpr2s)
    mean_tprs = tpr2s.mean(axis=0)
    auc_mean = "%.2f" % numpy.array(aucs).mean()
    with open(auc_path, 'w') as fout:
        fout.write(auc_mean)
    ax.plot(base_fpr, mean_tprs, 'b', label="auc: %s" % (auc_mean))
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('Receiver operating characteristic example')
    ax.legend(loc="lower right")
    fig.savefig(roc_path)

def main(argv):
    cv_proba_pkl_path = sys.argv[1]
    roc_path = sys.argv[2] #"roc.png"
    auc_path = os.path.join(os.path.dirname(roc_path), 'auc.txt') #"auc.txt"
    cv_probas = pickle.load(open(cv_proba_pkl_path, 'rb'))
    roc_plot(cv_probas, roc_path, auc_path)

if __name__ == "__main__":
    main(sys.argv[1:])

