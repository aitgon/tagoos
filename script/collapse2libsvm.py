import csv
import sys

input_path=sys.argv[1] #"collapse.bed"
variable_path=sys.argv[2] #"variable.txt"
instance_path=sys.argv[3] # "instance.txt"
libsvm_path=sys.argv[4] # "annot.libsvm"


label = "-1"

reader = csv.reader(open(input_path, 'r', encoding='utf-8'), delimiter="\t")
variable2i={}
for i,variable in enumerate(csv.reader(open(variable_path, 'r', encoding='utf-8'))):
    #print(i,variable)
    variable2i[variable[0]]=i+1
last_variable = variable[0]
last_variable_index=variable2i[last_variable] # needs for bug in xgboost

with open(instance_path, 'w') as instance_fout, open(libsvm_path, 'w') as libsvm_fout:
    for line in reader:
        if len(line)==4:
            chrom = line[0]
            start = str(int(line[1]) + 1)
            end = line[2]
            feature_list = line[3].split(',')
        else:
            sys.exit(1)
        instance_fout.write("%s:%s-%s\n"%(chrom, start, end)) # write previous instance
        feature_vector_str=":1 ".join([str(variable2i[f]) for f in feature_list]) + ":1"
        if not last_variable in feature_list: feature_vector_str = feature_vector_str + " %d:0"%last_variable_index
        libsvm_fout.write(label + " " + feature_vector_str + "\n")

