import pandas
import pickle
import os
import sys
import xgboost

def main(argv):
    annotation_libsvm = sys.argv[1]
    model_pkl = sys.argv[2] #"roc.png"import pandas
    score_tsv = sys.argv[3]
    #
    #feature_names = pandas.read_table("variable.txt", header=None)[0].tolist()
    instance = os.path.join(os.path.dirname(annotation_libsvm), "instance.txt")
    instance = pandas.read_csv(instance, header=None)
    model = pickle.load(open(model_pkl, "rb"))
    #import pdb; pdb.set_trace()
    xdm = xgboost.DMatrix(annotation_libsvm, feature_names=model.feature_names)
    #xdm = xgboost.DMatrix(annotation_libsvm)
    proba = model.predict(xdm)
    score=pandas.DataFrame({"rsid": instance[0].tolist(), "score": proba.tolist()})
    score.sort_values(by=["score", "rsid"], ascending=[False, True], inplace=True)
    score.to_csv(score_tsv, sep="\t", header=False, index=False, float_format='%.6f')

if __name__ == "__main__":
    main(sys.argv[1:])

