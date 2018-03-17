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
for i,variable in enumerate(csv.reader(open(variable_path, 'r'))):
    print(i,variable)
    variable2i[variable[0]]=i+1
last_variable_index=max(variable2i.values()) # needs for bug in xgboost

previous_instance = None
previous_label = None
libsvm_line = None
libsvm_list = None
variable_last_index_visited = False


#import pdb; pdb.set_trace()

with open(instance_path, 'w') as instance_fout, open(libsvm_path, 'w') as libsvm_fout:
    for line in reader:
        if len(line)==2: # there is only instance and variable, score=1 and label=-1
            instance = line[0]
            variable = line[1]
        elif len(line)==4:
            instance = line[0]
            score = line[2]
            variable = line[1]
            label = line[3]
        else:
            sys.exit(1)
        if instance != previous_instance: # if is a NEW instance, init libsvm_list
            #libsvm_fout.write(" ".join(sorted(libsvm_list)) + "\n") #write to stdout
            if not libsvm_list is None: # libsvm_list is not empty as for first line
                if not variable_last_index_visited: libsvm_list.append((last_variable_index, '0'))
                #import pdb; pdb.set_trace()
                libsvm_fout.write(label + " " + " ".join([":".join(str(x) for x in sublist) for sublist in sorted(libsvm_list)]) + "\n")
                instance_fout.write(previous_instance + "\n") # write previous instance
                variable_last_index_visited=False
            if variable=='':
                import pdb; pdb.set_trace()
            libsvm_list = [(variable2i[variable], score)] # new tuple to store variable:scores indices
            if variable2i[variable] == last_variable_index: variable_last_index_visited=True
        else:  # if is NOT A NEW instance
            if label != previous_label:
                raise Exception('One instance with two different labels -> check your TSV!. Quitting...')
                sys.quit() #
            try:
                libsvm_list.append((variable2i[variable], score)) # new tuple to store variable:scores indices
            except KeyError:
                raise("dfqsdfq")
            if variable2i[variable] == last_variable_index: variable_last_index_visited=True
        #import pdb; pdb.set_trace()
        previous_instance = instance
        previous_label = label
    if not variable_last_index_visited: libsvm_list.append((last_variable_index, '0'))
    libsvm_fout.write(label + " " + " ".join([":".join(str(x) for x in sublist) for sublist in sorted(libsvm_list)]) + "\n")
    instance_fout.write(previous_instance + "\n") # write previous instance

#            import pdb; pdb.set_trace()
#            if not libsvm_line is None: # libsvm_line was initiated
#                if not variable_last_index_visited: libsvm_line += " %d:0"%(last_variable_index)
#                instance_fout.write(previous_instance + "\n") # write previous instance
#                libsvm_fout.write(libsvm_line + "\n") # write previous line
#            libsvm_line = "%s %s:%s"%(label, variable2i[variable], score)
#            if variable2i[variable] == last_variable_index: variable_last_index_visited=True
#        else:  # if is NOT A NEW instance
#            libsvm_line += " %s:%s"%(variable2i[variable], score)
#    if not libsvm_line is None:
#        if not variable_last_index_visited: libsvm_line += " %d:0"%(last_variable_index)
#        instance_fout.write(previous_instance + "\n")
#        libsvm_fout.write(libsvm_line + "\n")

