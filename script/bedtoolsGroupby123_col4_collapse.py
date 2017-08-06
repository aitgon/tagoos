import csv
import sys

input_path=sys.argv[1] #"h.tsv"
output_path=sys.argv[2] #"variable.txt"

reader = csv.reader(open(input_path, 'r', encoding='utf-8'), delimiter="\t")

feature=None
previous_feature=None
bin_chrom=None
bin_start=None
bin_end=None
with open(output_path, 'w') as fout:
    for line in reader:
        if len(line)==4:
            chrom = line[0]
            start = line[1]
            end = line[2]
            feature = line[3]
        else:
            sys.exit(1)
        if feature != previous_feature: # if new feature
            if not bin_chrom is None:
                #print("%s\t%s\t%s\t%s\n"%(bin_chrom, bin_start, bin_end, previous_feature))
                fout.write("%s\t%s\t%s\t%s\n"%(bin_chrom, bin_start, bin_end, previous_feature))
            bin_chrom=chrom
            bin_start=start
            bin_end=end
            previous_feature=feature
        else:  # same as previous features
            bin_end=end

    if bin_chrom is None:
        fout.write("")
    else:
    #print("%s\t%s\t%s\t%s\n"%(bin_chrom, bin_start, bin_end, previous_feature))
        fout.write("%s\t%s\t%s\t%s\n"%(bin_chrom, bin_start, bin_end, previous_feature))

