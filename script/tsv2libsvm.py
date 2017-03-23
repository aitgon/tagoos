# sort input file first: sort 
# https://github.com/zygmuntz/phraug/blob/master/csv2libsvm.py
# http://fastml.com/processing-large-files-line-by-line/
import csv
import sys

tsv_path=sys.argv[1] #"h.tsv"
variable_path=sys.argv[2] #"variable.txt"
instance_path=sys.argv[3] # "instance.txt"
libsvm_path=sys.argv[4] # "annot.libsvm"


label = "-1"
score = "1"

reader = csv.reader(open(tsv_path, 'r'), delimiter="\t")
variable2i={}
for i,variable in enumerate(csv.reader(open(variable_path, 'r'))): variable2i[variable[0]]=i+1
last_variable_index=i # needs for bug in xgboost

visited_instance = None
libsvm_line = None
variable_last_index_visited = False


with open(instance_path, 'w') as instance_fout, open(libsvm_path, 'w') as libsvm_fout:
    for line in reader:
        if len(line)==2:
            instance = line[0]
            variable = line[1]
        elif len(line)==4:
            instance = line[0]
            score = line[1]
            variable = line[2]
            label = line[3]
        else:
            sys.exit(1)
        if instance != visited_instance: # if is new instance
            if not libsvm_line is None:
                if not variable_last_index_visited: libsvm_line += " %d:0"%(last_variable_index)
                instance_fout.write(visited_instance + "\n") # write previous instance
                libsvm_fout.write(libsvm_line + "\n") # write previous line
            libsvm_line = "%s %s:%s"%(label, variable2i[variable], score)
            if variable2i[variable] == last_variable_index: variable_last_index_visited=True
        else:
            libsvm_line += " %s:%s"%(variable2i[variable], score)
        visited_instance = instance
    if not libsvm_line is None:
        if not variable_last_index_visited: libsvm_line += " %d:0"%(last_variable_index)
        instance_fout.write(visited_instance + "\n")
        libsvm_fout.write(libsvm_line + "\n")

