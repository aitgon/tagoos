import pandas
import pickle
import os
import sys
import xgboost

def main(argv):
    annotation_libsvm_path = sys.argv[1]
    instance_txt_path = sys.argv[2]
    model_pkl_path = sys.argv[3] #"roc.png"import pandas
    score_tsv_path = sys.argv[4]
    #
    #feature_names = pandas.read_table("variable.txt", header=None)[0].tolist()
    #instance = os.path.join(os.path.dirname(annotation_libsvm), "instance.txt")
    instance = pandas.read_csv(instance_txt_path, header=None)
    model = pickle.load(open(model_pkl_path, "rb"))
    xdm = xgboost.DMatrix(annotation_libsvm_path, feature_names=model.feature_names)
    #xdm = xgboost.DMatrix(annotation_libsvm)
    proba = model.predict(xdm)
    score=pandas.DataFrame({"rsid": instance[0].tolist(), "score": proba.tolist()})
    score.sort_values(by=["score", "rsid"], ascending=[False, True], inplace=True)
    score.to_csv(score_tsv_path, sep="\t", header=False, index=False, float_format='%.3f')

if __name__ == "__main__":
    main(sys.argv[1:])

