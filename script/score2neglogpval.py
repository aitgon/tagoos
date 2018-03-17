

# sort scores first
import csv
import pandas
import sys

score_path = sys.argv[1]
score2pval2log2pval_path = sys.argv[2]
neglogpval_path = sys.argv[3]

df=pandas.read_csv(score2pval2log2pval_path, sep="\t", header=None)


reader = csv.reader(open(score_path, 'r'), delimiter="\t")

#percentile_old=None
with open(neglogpval_path, 'w') as fout:
    for genomeid,score in reader:
        score=float(score)
        pval = float(df.ix[(df[0]-score).abs().argsort()[:1],1])
        neglogpval = float(df.ix[(df[0]-score).abs().argsort()[:1],2])
        fout.write("%s\t%f\t%f\n"%(genomeid,pval,neglogpval))

