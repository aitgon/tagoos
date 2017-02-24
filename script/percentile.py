# sort scores first
import csv
import sys

score_path=sys.argv[1] #"h.tsv"
percentile_path=sys.argv[2] #"percentile.tsv"

num_lines = sum(1 for line in open(score_path))

reader = csv.reader(open(score_path, 'r'), delimiter="\t")

with open(percentile_path, 'w') as fout:
    for i,line in enumerate(reader):
        rsid = line[0]
        score = line[1]
        percentile = round((num_lines-i)/num_lines*100,2)
        fout.write("%s\t%s\t%.2f\n"%(rsid,score,percentile))

