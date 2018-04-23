#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tsv2libsvm(args):
    variable_max = 0
    with open(args.tsv) as fin:
        for line in fin:
            variable = int(line.split()[2])
            if variable > variable_max:
                variable_max = variable

    previous_instance, previous_label = None, None
    variable_list = []
    variable_level_list = []
    with open(args.tsv) as fin:
        for line in fin:
            instance = line.strip().split()[0]
            label = int(line.strip().split()[1])
            variable = int(line.strip().split()[2])
            variable_level = float(line.strip().split()[3])
            # Finished this instance
            if instance != previous_instance and variable_list != []:
                if not variable_max in variable_list:
                    variable_list.append(variable_max)
                    variable_level_list.append(0)
                out_line = "%s "%str(previous_label) + " ".join([":".join(str(x) for x in item) for item in zip(variable_list, variable_level_list)])
                args.instance.write(str(previous_instance) + "\n")
                args.libsvm.write(out_line + "\n")
                variable_list = []
                variable_level_list = []
            # Raise error if a variable is duplicated for one instance
            if variable in variable_list:
                raise AssertionError("Error: Duplicated variable %d for instance %s"%(variable,instance))
            variable_list.append(variable)
            variable_level_list.append(variable_level)
            previous_instance, previous_label = instance, label

        # After last line
        if not variable_max in variable_list:
            variable_list.append(variable_max)
            variable_level_list.append(0)
        out_line = "%s "%str(previous_label) + " ".join([":".join(str(x) for x in item) for item in zip(variable_list, variable_level_list)])
        args.instance.write(str(previous_instance) + "\n")
        args.libsvm.write(out_line + "\n")

import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tsv', dest='tsv', default=sys.stdin)
    parser.add_argument('--instance', dest='instance', type=argparse.FileType('w'))
    parser.add_argument('--libsvm', dest='libsvm', type=argparse.FileType('w'))
    args = parser.parse_args()
    # ... do something with args.input ...
    tsv2libsvm(args)

if __name__ == '__main__':
    main()



