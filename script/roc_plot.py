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

def roc_plot(y_test_proba_path_list, roc_path, auc_path):
    fprs = []
    tprs = []
    tpr2s = []
    aucs = []
    base_fpr = numpy.linspace(0, 1, 101)
    fig, ax = pyplot.subplots()
    cv_rocs = {}
    #for chrom in sorted(cv_probas.keys()):
    for i,y_test_proba_path in enumerate(y_test_proba_path_list):
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
        cv_rocs[i] = {'fpr': fpr, 'tpr': tpr, 'thresholds': thresholds}
        ax.plot(fpr, tpr, 'b', alpha=0.05)
    tpr2s = numpy.array(tpr2s)
    mean_tprs = tpr2s.mean(axis=0)
    auc_mean = "%.2f" % numpy.array(aucs).mean()
    with open(auc_path, 'w') as fout:
        fout.write(auc_mean)
    ax.plot(base_fpr, mean_tprs, 'b', label="auc: %s" % (auc_mean))
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel('False positive rate',fontsize=20)
    ax.set_ylabel('True positive rate',fontsize=20)
    ax.set_title('ROC curve',fontsize=20)
    ax.legend(loc="lower right",prop={'size':20})
    fig.savefig(roc_path)

def main(argv):
    y_test_proba_path_list = sys.argv[1:-1]
    roc_path = sys.argv[-1]
    #cv_proba_pkl_path = sys.argv[1]
    #roc_path = sys.argv[2] #"roc.png"
    auc_path = os.path.join(os.path.dirname(roc_path), 'auc.txt') #"auc.txt"
    #cv_probas = pickle.load(open(cv_proba_pkl_path, 'rb'))
    roc_plot(y_test_proba_path_list, roc_path, auc_path)

if __name__ == "__main__":
    main(sys.argv[1:])

