# Code notes

## EUR splitted

python

~~~
import pandas
import xgboost
variable = pandas.read_table("out_eur/variable.tsv", header=None)
variable.sort_values(by=0, inplace=True)
feature_names = ['label'] + variable[1].tolist()
xdm = xgboost.DMatrix("out_eur/annotation.libsvm", feature_names=features_names)
params = {'silent': True}
model = xgboost.train(params, xdm)
~~~

~~~
export INDEX2ANNOT_R2_TSV=out_eur/index2annot_r2_label.tsv
export OUTDIR=out_eur
Rscript tsv2libsvm.R
~~~

~~~
export OUTDIR_PREFIX=out_eur2/
Rscript -e 'library(data.table); dt = fread("out_eur/pos_index2annot_r2.tsv", sep="\t"); dt$label = 1; fwrite(dt, file="out_eur/pos_index2annot_r2_label.tsv", sep="\t", row.names=FALSE, col.names=FALSE)'
find $PWD/out_eur/pos/. -type f -name "index2annot_r2.tsv" |while read F; do cat $F; done >out_eur/pos_index2annot_r2.tsv
Rscript -e 'library(data.table); dt = fread("out_eur/neg_index2annot_r2.tsv", sep="\t"); dt$label = -1; fwrite(dt, file="out_eur/neg_index2annot_r2_label.tsv", sep="\t", row.names=FALSE, col.names=FALSE)'
find $PWD/out_eur/neg/. -type f -name "index2annot_r2.tsv" |while read F; do cat $F; done >out_eur/neg_index2annot_r2.tsv
~~~

Positive

~~~
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export TAG_RSID=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export OUTDIR_PREFIX=out_eur/pos/
#
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; export OUTDIR=${OUTDIR_PREFIX}/${CHR}; mkdir -p $OUTDIR; export LD=$GENOME1K_DATA_DIR/chr${CHR}/chr${CHR}_ld.ld; export INDEX_RSID=$GENOME1K_DATA_DIR/chr${CHR}/chr${CHR}_index.prune.in; echo chr$CHR;  Rscript ldlocus.R'
#
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed; export ANNOTDIR=out_$(basename ${ANNOT_BED%_1col.bed})/${CHR}; export OUTDIR=${OUTDIR_PREFIX}/${CHR}; echo $CHR; Rscript annotate_ldlocus.R'
#
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; echo $CHR; export OUTDIR=${OUTDIR_PREFIX}/${CHR}; export INDEX2ANNOT_R2_RDA=${OUTDIR}/index2annot_r2.Rda ; export LABEL=1; Rscript tsv2libsvm.R'
~~~

Negative

~~~
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export TAG_RSID=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg1000000.rsid
export OUTDIR_PREFIX=out_eur2/neg/
#
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; export OUTDIR=${OUTDIR_PREFIX}/${CHR}; mkdir -p $OUTDIR; export LD=$GENOME1K_DATA_DIR/chr${CHR}/chr${CHR}_ld.ld; export INDEX_RSID=$GENOME1K_DATA_DIR/chr${CHR}/chr${CHR}_index.prune.in; echo chr$CHR;  Rscript ldlocus.R'
#
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed; export ANNOTDIR=out_$(basename ${ANNOT_BED%_1col.bed})/${CHR}; export OUTDIR=${OUTDIR_PREFIX}/${CHR}; echo $CHR; Rscript annotate_ldlocus.R'
#
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; echo $CHR; export OUTDIR=${OUTDIR_PREFIX}/${CHR}; export INDEX2ANNOT_R2_RDA=${OUTDIR}/index2annot_r2.Rda ; export LABEL=-1; Rscript tsv2libsvm.R'
~~~

<!--# ------------------>

<!--Convert to libsvm format-->

<!--~~~-->
<!--date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; echo $CHR; export LDLOCUSDIR=out_ld/${CHR}; export INDEX2ANNOT_R2_RDA=${LDLOCUSDIR}/index2annot_r2.Rda ; export LABEL=1; Rscript tsv2libsvm.R'-->
<!--~~~-->

<!--Annotate LD loci-->

<!--~~~-->
<!--date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed; export ANNOTDIR=out_$(basename ${ANNOT_BED%_1col.bed})/${CHR}; export LDLOCUSDIR=out_ld/${CHR}; echo $CHR; Rscript annotate_ldlocus.R &>$LDLOCUSDIR/out_annotate_ld.log'-->
<!--~~~-->

<!--LD Create LD loci, eur (chrom-wise)-->

<!--~~~-->
<!--export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes-->
<!--export TAG_RSID=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid-->
<!--date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; export OUTDIR=out_ld/${CHR}; mkdir -p $OUTDIR; export LD=$GENOME1K_DATA_DIR/chr${CHR}/chr${CHR}_ld.ld; export INDEX_RSID=$GENOME1K_DATA_DIR/chr${CHR}/chr${CHR}_index.prune.in; echo chr$CHR;  Rscript ldlocus.R &>$OUTDIR/out.log;'-->
<!--~~~-->

Create eur, annotation_1col.bed (chrom-wise)

~~~
export ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
date; printf %s\\n {1..22} | xargs -I{} -n 1 -P 16 sh -c 'export CHR={}; export OUTDIR=out_$(basename ${ANNOT_BED%_1col.bed})/{}; mkdir -p $OUTDIR; bash annotate.sh $CHR $ANNOT_BED $OUTDIR'
~~~

## EUR, all annotations, all steps to sparse matrix

Annotate LD loci

~~~
CHR=eur
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
export ANNOTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
export LDLOCUSDIR=out_ld_${CHR}

Rscript annotate_ldlocus.R &>$OUTDIR/out.log
~~~

Create LD loci,eur

~~~
GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
CHR=eur
mkdir -p $OUTDIR
export OUTDIR=$OUTDIR
export LD=$GENOME1K_DATA_DIR/${CHR}/${CHR}_ld.ld
export INDEX_RSID=$GENOME1K_DATA_DIR/${CHR}/${CHR}_index.prune.in
export TAG_RSID=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
OUTDIR=out_ld_${CHR}

Rscript ldlocus.R &>$OUTDIR/out.log
~~~

Create eur, annotation_1col.bed

~~~
export ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
export OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
printf %s\\n {21..22} | xargs -I{} -n 1 -P 1 sh -c 'export OUTDIR=out_{}_$(basename ${ANNOT_BED%_1col.bed}); bash annotate.sh $CHR $ANNOT_BED $OUTDIR'

CHRMAX=2
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
for i in $(seq 1 $CHRMAX); do
echo $i; 
done


OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
mkdir -p $OUTDIR
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR &>$OUTDIR/out.log
~~~

## Chrom 1, all annotations, all steps to sparse matrix

Annotate LD loci

~~~
CHR=chr1
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
export ANNOTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
export LDLOCUSDIR=out_ld_${CHR}

Rscript annotate_ldlocus.R &>$OUTDIR/out.log
~~~

Create LD loci, chr 1

~~~
GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
CHR=chr1
OUTDIR=out_ld_${CHR}
mkdir -p $OUTDIR
export OUTDIR=$OUTDIR
export LD=$GENOME1K_DATA_DIR/${CHR}/${CHR}_ld.ld
export INDEX_RSID=$GENOME1K_DATA_DIR/${CHR}/${CHR}_index.prune.in
export TAG_RSID=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid

Rscript ldlocus.R &>$OUTDIR/out.log
~~~

Create chr1, annotation_1col.bed

~~~
CHR=chr1
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
mkdir -p $OUTDIR
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR &>$OUTDIR/out.log
~~~

Create chr1, annotation_1col.bed

~~~
CHR=chr1
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
mkdir -p $OUTDIR
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR &>$OUTDIR/out.log
~~~

# Archive 2


## Annotate LD locus

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/exceptEncode2_1col.bed
export ANNOTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
export LDLOCUSDIR=out_ld_${CHR}


Rscript annotate_ldlocus.R
~~~

## Annotation

Test chr22, annotation_1col.bed

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
mkdir -p $OUTDIR
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR &>$OUTDIR/out.log
~~~

Test chr22, exceptEncode2_1col.bed

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/exceptEncode2_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR &>$OUTDIR/out.log
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
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED%_1col.bed})
time bash annotate.sh $CHR $ANNOT_BED $OUTDIR
# 16 s
~~~

# Requirments

~~~
Rscript -e 'install.packages(c("data.table"), lib="/cobelix/gonzalez/Software/R-packages", repos="http://stat.ethz.ch/CRAN/")'
~~~

