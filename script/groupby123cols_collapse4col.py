import csv
import sys

input_path=sys.argv[1] #"h.tsv"
output_path=sys.argv[2] #"variable.txt"

reader = csv.reader(open(input_path, 'r', encoding='utf-8'), delimiter="\t")


prev_chrom = None
prev_start = None
prev_end = None
prev_annotation = None
annotation_list = []
with open(output_path, 'w') as fout:
    for line in reader:
        if len(line)==4:
            chrom = line[0]
            start = line[1]
            end = line[2]
            annotation = line[3]
        else:
            sys.exit(1)
        # two or more different annotations in this peak
        if chrom == prev_chrom and start == prev_start and end == prev_end:
            annotation_list.append(annotation)
        else: # new peak
            if not prev_chrom is None:
                fout.write("%s\t%s\t%s\t%s\n"%(prev_chrom, prev_start, prev_end, ",".join(annotation_list)))
            prev_chrom = chrom
            prev_start = start
            prev_end = end
            annotation_list = [annotation]

    if prev_chrom is None:
        fout.write("")
    else:
        fout.write("%s\t%s\t%s\t%s\n"%(prev_chrom, prev_start, prev_end, ",".join(annotation_list)))

