import matplotlib; matplotlib.use('Agg')
import pandas
import pickle
import sys
import xgboost

from matplotlib import pyplot
from pylab import arange

#fin_libsvm = "annotation.libsvm"
#fin_variable = "variable.txt"
##
#model_path = "model.pkl"
#feature_path = "feature_importance.tsv"
#feature_importance_png = "feature_importance.png"

def main(argv):
    # print command line arguments
    fin_libsvm = sys.argv[1]
    fin_variable = sys.argv[2]
    model_path = sys.argv[3]
    feature_path = sys.argv[4]
    feature_importance_png = sys.argv[5]
    #
    variable = pandas.read_csv(fin_variable, header=None)
    #variable.sort_values(by=[0], inplace=True)
    variable = ['label'] + variable[0].tolist()
    # Model ----------------------------
    xgdmat = xgboost.DMatrix(fin_libsvm, feature_names=variable)
    params={'silent': True}
    model = xgboost.train(params, xgdmat)
    pickle.dump(model, open(model_path, "wb"))
    # Feature importance ----------------------------
    feature_importance = pandas.DataFrame.from_records(list(model.get_score(importance_type="gain").items()))
    feature_importance.columns = ['feature', 'weight']
    feature_importance = feature_importance.loc[:, ['feature', 'weight']]
    feature_importance.sort_values(by='weight', ascending=False, inplace=True)
    feature_importance.to_csv(feature_path, sep="\t", index=False, header=True)
    # Feature importance png ----------------------------
    features = feature_importance.feature.head(n=30).tolist()
    # Feature importance plot
    nb_features=30
    xlabel='Average gain'
    title = "xgboost feature importance"
    val=feature_importance.weight.head(nb_features).tolist()
    val.reverse()
    pos = arange(len(val))+.5    # the bar centers on the y axis
    labels=feature_importance.feature.head(nb_features).tolist()
    labels = [label_i[:50] for label_i in labels]
    labels.reverse()
    fig=pyplot.figure()
    ax1=fig.add_subplot(111)
    fig.subplots_adjust(left=0.65, bottom=0.15)
    ax1.barh(pos,val, align='center')
    pyplot.yticks(pos, labels, rotation=0)
    pyplot.xticks(rotation=40)
    pyplot.xlabel(xlabel)
    pyplot.title(title)
    pyplot.grid(True)
    pyplot.savefig("%s"%feature_importance_png)

if __name__ == "__main__":
    main(sys.argv[1:])

