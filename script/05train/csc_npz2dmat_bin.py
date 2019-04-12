from scipy.sparse import csc_matrix, vstack
import os
import pandas
import scipy
import sys
import xgboost

TEST_CHROM=int(sys.argv[1])
REGION=sys.argv[2]
#TRAIN_CHROM_DIR="/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/{}/train/chrom/{}/index2label2annotationid2r2_label1.csc.npz"
TAGOOS_APPLI_DIR=sys.argv[3]#/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328

#variableid2variable_tsv = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/data/annotation/mergedannot/variableid2variable.tsv"
variableid2variable_tsv=sys.argv[4]
variableid2variable_df = pandas.read_csv(variableid2variable_tsv, sep="\t", header=None, names=["variableid", "variable"])
feature_names = variableid2variable_df.variable.tolist()
variableid_max = max(variableid2variable_df.variableid)

test_label_1_csc_npz = sys.argv[5]
test_label_0_csc_npz = sys.argv[6]
test_label_1_csc = scipy.sparse.load_npz(test_label_1_csc_npz)
test_label_1_label = [1] * test_label_1_csc.shape[0]
test_label_0_csc = scipy.sparse.load_npz(test_label_0_csc_npz)
test_label_0_label = [0] * test_label_0_csc.shape[0]

#REGION="intronic"
# input
#test_label_1_csc_npz = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/{}/train/test/chrom/{}/index2label2annotationid_label1.csc.npz".format(REGION, TEST_CHROM)
#test_label_0_csc_npz = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/{}/train/test/chrom/{}/index2label2annotationid_label0.csc.npz".format(REGION, TEST_CHROM)
# output
#dtrain_bin = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/{}/train/chrom/{}/dtrain.bin".format(REGION, TEST_CHROM)
#dtest_bin = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/{}/train/test/chrom/{}/dtest.bin".format(REGION, TEST_CHROM)
dtrain_bin = sys.argv[7]
dtest_bin = sys.argv[8]


def get_train_matrix_csc(test_chrom):
    train_csc = None
    train_label = None
    if test_chrom % 6 == 0:
        train_chrom_list = list(range(6,23,6))
    if test_chrom % 6 == 1:
        train_chrom_list = list(range(1,23,6))
    if test_chrom % 6 == 2:
        train_chrom_list = list(range(2,23,6))
    if test_chrom % 6 == 3:
        train_chrom_list = list(range(3,23,6))
    if test_chrom % 6 == 4:
        train_chrom_list = list(range(4,23,6))
    if test_chrom % 6 == 5:
        train_chrom_list = list(range(5,23,6))
    for train_chrom in train_chrom_list:
        if train_chrom != test_chrom:
            #print(test_chrom,train_chrom)
            train_chrom_i_label_1_csc_npz = os.path.join(TAGOOS_APPLI_DIR, "out/{}/train/chrom/{}/index2label2annotationid2r2_label1.csc.npz".format(REGION, train_chrom))
            #print(train_chrom_i_label_1_csc_npz)
            train_chrom_i_label_1_csc = scipy.sparse.load_npz(train_chrom_i_label_1_csc_npz)
            train_chrom_i_label_1 = [1] * train_chrom_i_label_1_csc.shape[0]
            train_chrom_i_label_0_csc_npz = os.path.join(TAGOOS_APPLI_DIR, "out/{}/train/chrom/{}/index2label2annotationid2r2_label0.csc.npz".format(REGION, train_chrom))
            #print(train_chrom_i_label_0_csc_npz)
            train_chrom_i_label_0_csc = scipy.sparse.load_npz(train_chrom_i_label_0_csc_npz)
            train_chrom_i_label_0 = [0] * train_chrom_i_label_0_csc.shape[0]
            if train_csc is None: # 
                train_csc = vstack([train_chrom_i_label_1_csc, train_chrom_i_label_0_csc])
                train_label = train_chrom_i_label_1 + train_chrom_i_label_0
            else:
                train_csc = vstack([train_csc, train_chrom_i_label_1_csc, train_chrom_i_label_0_csc])
                train_label = train_label + train_chrom_i_label_1 + train_chrom_i_label_0
    return train_csc, train_label


train_csc, train_label = get_train_matrix_csc(TEST_CHROM)


dtrain = xgboost.DMatrix(data=train_csc, label=train_label, feature_names=['label'] + feature_names, silent=True)
dtrain.save_binary(fname=dtrain_bin)

dtest = xgboost.DMatrix(data=vstack([test_label_1_csc, test_label_0_csc]), label=test_label_1_label + test_label_0_label, feature_names=['label'] + feature_names, silent=True)
dtest.save_binary(fname=dtest_bin)


