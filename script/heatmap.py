import matplotlib; matplotlib.use('Agg')
import os
import pandas
import pickle
from matplotlib import pyplot
import seaborn
import sys

def main(argv):
    fin_index2annot_r2_label_tsv = sys.argv[1]
    fin_model_pkl = sys.argv[2]
    fout_heatmap_png = sys.argv[3]
    #
    # Get best variables from model
    model = pickle.load(open(fin_model_pkl, "rb"))
    variable_importance = pandas.DataFrame.from_records(list(model.get_score(importance_type="gain").items()))
    variable_importance.columns = ['variable', 'weight']
    variable_importance = variable_importance.loc[:, ['variable', 'weight']]
    variable_importance.sort_values(by='weight', ascending=False, inplace=True)
    variable = variable_importance.variable.head(n=30).tolist()

    # Create matrix
    dat=pandas.read_csv(fin_index2annot_r2_label_tsv, sep="\t", header=None)
    dat.columns = ['rsid', 'r2', 'variable', 'label']
    # select best variables
    dat=dat.loc[dat.variable.isin(variable),]
    dat.sort_values(by=['rsid', 'variable', 'label', 'r2'], ascending=[False, False, False, False], inplace=True)
    dat.drop_duplicates(subset=['rsid', 'variable'], keep='first', inplace=True)

    dat=pandas.pivot_table(dat, values="r2", index=["rsid", "label"], columns='variable')
    dat.reset_index(inplace=True)
    dat.fillna(0, inplace=True)

    #
    # Create color palette
    dat_label = dat.label.sort_values(ascending=True).unique()
    network_pal = seaborn.light_palette('red', len(dat_label))
    network_lut = dict(zip(dat_label, network_pal))
    network_colors = pandas.Series(dat.label).map(network_lut)

    # Cluster heatmap
    sys.setrecursionlimit(max(dat.shape))
    print("heatmap cluster")
    g = seaborn.clustermap((dat.loc[:,variable]).transpose(), col_colors=network_colors)
    pyplot.setp(g.ax_heatmap.get_xticklabels(), visible=False)
    pyplot.setp(g.ax_heatmap.get_yticklabels(), visible=True, rotation=0)
    g.savefig(fout_heatmap_png)
    outdir=os.path.dirname(fout_heatmap_png)
    clustermap_pkl_path = os.path.join(outdir, "clustermap.pkl")
    pickle.dump(g, open(clustermap_pkl_path, "wb"))

if __name__ == "__main__":
    main(sys.argv[1:])

