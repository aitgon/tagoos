#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import io
import sys
import tempfile
import unittest

input_bed ="""chr10	94898	94899	.
chr10	94899	94900	.
chr10	94900	94901	.
chr10	94901	94902	annot3
chr10	94902	94903	annot3
chr10	94903	94904	annot3
chr10	94904	94905	annot3
chr10	94905	94906	annot3
chr10	94906	94907	annot3
chr10	94907	94908	annot3
chr10	94908	94909	annot3
chr10	94909	94910	annot3
chr10	94910	94911	.
chr10	180404	180405	annot1,annot2
chr10	180405	180406	annot3
"""

output_bed = """chr10	94898	94901	.
chr10	94901	94910	annot3
chr10	94910	94911	.
chr10	180404	180405	annot1,annot2
chr10	180405	180406	annot3
"""

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = create_parser()

    def test_parser(self,):
        fin = io.StringIO(input_bed)
        output = tempfile.NamedTemporaryFile().name
        with open(output, "w") as fout:
            myfunc(fin, fout)
        with open(output, "r") as fin:
            self.assertTrue(fin.read() == output_bed)


def myfunc(fin, fout=sys.stdout):
    prev_chrom, prev_start, prev_end, prev_annotation = None, None, None, None
    collapsed_chrom, collapsed_start, collapsed_end, collapsed_annotation = None, None, None, None
    for line in csv.reader(fin, delimiter="\t"): # read each line
        chrom,start,end,annotation = line
        if chrom == prev_chrom and start == prev_end and annotation == prev_annotation: # collapse it
            collapsed_chrom = chrom
            collapsed_end = end
            collapsed_annotation = annotation
        else: # collapse it:
            if not prev_chrom is None:
                fout.write("{}\t{}\t{}\t{}\n".format(collapsed_chrom, collapsed_start, collapsed_end, collapsed_annotation))
            collapsed_chrom = chrom
            collapsed_start = start
            collapsed_end = end
            collapsed_annotation = annotation
        prev_chrom = chrom
        prev_start = start
        prev_end = end
        prev_annotation = annotation
    fout.write("{}\t{}\t{}\t{}\n".format(collapsed_chrom, collapsed_start, collapsed_end, collapsed_annotation))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input', type = argparse.FileType('r'), default=sys.stdin, help="Input bed")
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'), default=sys.stdout)
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    myfunc(args.input, args.output)

if __name__ == '__main__':
    main()


