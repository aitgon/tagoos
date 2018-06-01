from sklearn import metrics
import pandas
import sys
import xgboost

param_set_0 = {
    'colsample_bytree': 1,  # option for logging
    'early_stopping_rounds': None,
    'eta': 0.3,
    'min_child_weight': 1, # 1,7,20 ~ 336
    'max_delta_step': 1,
    'max_depth': 6,
    'num_boost_round': 10,
    'nthread': 7,
    'objective': 'binary:logistic',
    'silent': True,  # option for logging
    'seed': 1357,  #
    'subsample': 1,  # option for logging
}


#variableid2variable_tsv = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/data/annotation/mergedannot/variableid2variable.tsv"
variableid2variable_tsv=sys.argv[4]
variableid2variable_df = pandas.read_csv(variableid2variable_tsv, sep="\t", header=None, names=["variableid", "variable"])
feature_names = variableid2variable_df.variable.tolist()
#
# output
auc_train_list = []
auc_test_list = []
#df = pandas.DataFrame({"test_chrom": [], "auc_train": [], "auc_test": []})
#
#test_chrom = 1
test_chrom = sys.argv[1]
#for test_chrom in list(range(1,2)):
#dtrain_bin = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/intergenic/train/chrom/{}/dtrain.bin".format(test_chrom)
dtrain_bin = sys.argv[2]
#dtest_bin = "/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/intergenic/train/test/chrom/{}/dtest.bin".format(test_chrom)
dtest_bin = sys.argv[3]

dtrain = xgboost.DMatrix(data=dtrain_bin, feature_names=['label'] + feature_names, silent=True)
dtest = xgboost.DMatrix(data=dtest_bin, feature_names=['label'] + feature_names, silent=True)

scale_pos_weight = (dtrain.get_label() == 0).sum() / (dtrain.get_label() == 1).sum()

scale_pos_weight = (dtrain.get_label() == 0).sum() / (dtrain.get_label() == 1).sum()
param_set_0['scale_pos_weight'] = scale_pos_weight

bst = xgboost.train(params=param_set_0, dtrain=dtrain, early_stopping_rounds=param_set_0['early_stopping_rounds'], num_boost_round=param_set_0['num_boost_round'])
nfeatures = len(list(bst.get_score(importance_type="gain").items()))
pred_train = bst.predict(dtrain)
pred_test = bst.predict(dtest)

fpr_train, tpr_train, thresholds_train = metrics.roc_curve(list(dtrain.get_label()), pred_train, pos_label=1)
auc_train = metrics.auc(fpr_train, tpr_train)

fpr_test, tpr_test, thresholds_test = metrics.roc_curve(dtest.get_label(), pred_test, pos_label=1)
auc_test = metrics.auc(fpr_test, tpr_test)

df_i = pandas.DataFrame({"test_chrom": [test_chrom], "auc_train": [auc_train], "auc_test": [auc_test]})

#df = pandas.concat([df, df_i], axis=0)
#
# write to output
auc_tsv=sys.argv[5]
df_i = df_i[["test_chrom", "auc_train", "auc_test"]]
df_i.to_csv(auc_tsv, sep="\t", index=False)


