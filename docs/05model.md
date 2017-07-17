# Model learning and DBSNP variant prediction

## GRASP database

In this example we create a model for

- Associated GRASP variants ($p-val lower than 10^8$)
- 100000 random variants for the 1000 genome DB
- The __annotationcorr__ variants
- The __index__ variants


Region variables

$REGION \in {'intronic', 'enhancer'}$

~~~
export REGION=intronic # default intronic
export CHROM="$(seq 22)"
~~~

Positive

~~~
export TAG_POS_RSID=$PWD/out/data/snp/grasp/${REGION}/grasp108.rsid
export POS_LABEL=GRASP108
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export LD=0.8
~~~

Negative

~~~
export NBNEG=1000000
export NEG_LABEL=1kg${NBNEG}
export TAG_NEG_RSID=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg${NBNEG}.rsid
~~~


~~~
export THREADS=16 # default 8
export QUEUE=batch # default batch
#
export TAG_POS_DIR=$PWD/out/${POS_LABEL}${REGION}/pos/${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_NEG_DIR=$PWD/out/neg/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}

#
export ANNOTATION_DIR=$PWD/out/data/annotation/${ANNOT_LABEL}
export GENOME1K_DIR=$PWD/out/data/snp/1000genomes
export GENOME1K_PEAKBED_DIR=$GENOME1K_DIR/${REGION}/peak_bed
export PYTHONBIN=$(which python)
export INDEX_DIR=$PWD/out/${INDEX_LABEL}
~~~

~~~
export TAG_DIR=$TAG_POS_DIR
export LABEL=1
export TAG_RSID=$TAG_POS_RSID
#
time snakemake -s   ${TAGOOS}/snakefile/model/rsid2chrom.yml -p -j 1 -c "qsub -X -V -d $TAG_DIR -q ${QUEUE} -l nodes=1:ppn={threads} -e $TAG_DIR/stderr.log -o $TAG_DIR/stdout.log" -d $TAG_DIR -p
~~~

POSITIVE 

~~~
time snakemake -s ${TAGOOS}/snakefile/model/tag.yml -p -j 32 -c "qsub -X -V -d $TAG_DIR -q ${QUEUE} -l nodes=1:ppn={threads} -e $TAG_DIR/stderr.log -o $TAG_DIR/stdout.log" -d $TAG_DIR --latency-wait 60 -pn
~~~

NEGATIVE

~~~
export TAG_DIR=$TAG_NEG_DIR
export LABEL=-1
export TAG_RSID=$TAG_NEG_RSID
#
time snakemake -s ${TAGOOS}/snakefile/model/tag.yml -p -j 32 -c "qsub -X -V -d $TAG_DIR -q ${QUEUE} -l nodes=1:ppn={threads} -e $TAG_DIR/stderr.log -o $TAG_DIR/stdout.log" -d $TAG_DIR --latency-wait 60 -pn
~~~

MODEL

~~~
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}
#
time snakemake -s ${TAGOOS}/snakefile/model/model.yml -p -j 32 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

SELECT FEATURES FROM ANNOTATION BED

~~~
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/annotation
export FEATURE_IMPORTANCE_TSV=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_public/feature_importance.tsv
export ANNOTATION_BED_IN=$PWD/out/data/annotation/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export ANNOTATION_BED_OUT=$OUTDIR/${ANNOT_LABEL}.bed
#
time snakemake -s ${TAGOOS}/snakefile/model/select_features.yml -p -j 32 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

SPLIT ANNOTATION BED WITH SELECTED FEATURES

~~~
export ANNOT_LABEL=mergedannot
#
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/annotation/${ANNOT_LABEL}.bed
export ANNOTATION_DIR=$(dirname ${ANNOTATION_BED})
#
export CHROM="$(seq 1 22) X"
time snakemake -s ${TAGOOS}/snakefile/data_annotation/split_annotation.yml -p -j 32 -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads} -e $ANNOTATION_DIR/stderr.log -o $ANNOTATION_DIR/stdout.log" -d $ANNOTATION_DIR -pn
~~~

ANNOTATE DBSNP VARIANTS

~~~
export CHROM="$(seq 1 22) X"
#
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/annotation/${ANNOT_LABEL}.bed
#
export ANNOTATION_DIR=$(dirname ${ANNOTATION_BED})
export SNP_DIR_IN=$PWD/out/data/snp/dbsnp/${REGION}
export SNP_DIR_OUT=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/dbsnp_annotation
export VARIABLE_TXT=/cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos-appli/170712/out/data/annotation/mergedannot/variable.txt
#
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/data_snp/annotate.yml -p -j $SNAKEMAKE_J -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads} -e $SNP_OUTDIR/stderr.log -o $SNP_OUTDIR/stdout.log" -d $SNP_OUTDIR -pn
~~~

SCORE DBSNP VARIANTS

~~~
export THREADS=16
export CHROM="$(seq 22)"
#export CHROM=$(cat $PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_model1/CV/selected_chroms.txt)
export MODEL_PKL=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}/model.pkl
#export ANNOTATION_DIR=$PWD/out/data/annotation/${ANNOT_LABEL}
#
export DBSNP_DIR=/cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos-appli/170712/out/GRASP108intronic/1kg1000000intronic_mergedannot_index3_data/dbsnp_annotation
export SCRIPT_DIR=${TAGOOS}/script
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_dbsnp

time snakemake -s ${TAGOOS}/snakefile/model/score.yml -j 32 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

