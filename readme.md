# Code notes

Test eur, annotation_1col.bed

~~~
CHR=eur
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR
~~~

Test chr22, exceptEncode2_1col.bed

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/exceptEncode2_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR
~~~

~~~
# Score

time python score.py $OUTDIR/annotation_matrix_rsid.tsv data/model.pkl $OUTDIR/score.tsv
# 20s
~~~

~~~
# Retrieve subset of matrix

head -n 1 $OUTDIR/annotation_matrix_rsid.tsv >$OUTDIR/test_matrix.tsv
/gpfs/tgml/apps/get_record $OUTDIR/annotation_matrix_rsid.tsv.idx  $OUTDIR/annotation_matrix_rsid.tsv -f data/$CHR.rsid >>$OUTDIR/test_matrix.tsv
~~~

Test chr22, youngh3k27ac_1col.bed

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR
# 16 s
~~~

# Requirments

~~~
Rscript -e 'install.packages(c("data.table"), lib="/cobelix/gonzalez/Software/R-packages", repos="http://stat.ethz.ch/CRAN/")'
~~~

