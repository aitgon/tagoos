#!/bin/bash

CHR=chr$1
ANNOT_BED=$2
OUTDIR=$3

GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
SNP_BED=$GENOME1K_DATA_DIR/${CHR}/${CHR}.peak.bed
TMPFILE=$(mktemp /tmp/abc-script.XXXXXX)

echo $CHR
mkdir -p $OUTDIR
time intersectBed -sorted -a ${SNP_BED} -b ${ANNOT_BED} -wb |awk 'BEGIN{OFS="\t"}{print $4,$8}' >$OUTDIR/annotated.tsv

