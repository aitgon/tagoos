# Code notes

Test chr22, exceptEncode2_1col.bed

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/exceptEncode2_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate_1kg.sh $CHR $ANNOT_BED $OUTDIR
~~~

~~~
# Retrieve rsid annotation

/gpfs/tgml/apps/get_record $OUTDIR/annotation_matrix_rsid.tsv.idx  $OUTDIR/annotation_matrix_rsid.tsv -f data/$CHR.rsid
~~~

Test chr22, youngh3k27ac_1col.bed

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate_1kg.sh $CHR $ANNOT_BED $OUTDIR
# 16 s
~~~

# Requirments

~~~
Rscript -e 'install.packages(c("data.table"), lib="/cobelix/gonzalez/Software/R-packages", repos="http://stat.ethz.ch/CRAN/")'
~~~

