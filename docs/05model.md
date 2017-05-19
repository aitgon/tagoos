# Model learning and DBSNP variant prediction

## GRASP database

In this example we create a model for

- Associated GRASP variants ($p-val lower than 10^8$)
- 100000 random variants for the 1000 genome DB
- The __annotationcorr__ variants
- The __index__ variants


These are the possible __REGION__ variables:

$REGION \in {'genomic', 'intronic', 'intergenprox', 'intergendistal'}$

Positive

~~~
export REGION=genomic # default genomic
export TAG_POS_RSID=$HOME/data/2015_svmgwas/data/variant/grasp/${REGION}/grasp108.rsid
export POS_LABEL=GRASP108
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export LD=0.8
~~~

Negative

~~~
export NEG_LABEL=GRASP105
export TAG_NEG_RSID=$HOME/data/2015_svmgwas/data/variant/grasp/${REGION}/grasp105.rsid
~~~

~~~
export NBNEG=1000000
export NEG_LABEL=1kg${NBNEG}
export TAG_NEG_RSID=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg1kg${NBNEG}.rsid
~~~


~~~
export THREADS=8 # default 8
#
export TAG_POS_DIR=$PWD/out/${POS_LABEL}${REGION}/pos/${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_NEG_DIR=$PWD/out/neg/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}

#
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export GENOME1K_PEAKBED_DIR=$GENOME1K_DIR/${REGION}/peak_bed
export INDEX_DIR=$PWD/out/${INDEX_LABEL}
export PYTHONBIN=$(which python)
export SCRIPT_DIR=${TAGOOS}/script
~~~

~~~
export TAG_DIR=$TAG_POS_DIR
export LABEL=1
export TAG_RSID=$TAG_POS_RSID
#
time snakemake -s   ${TAGOOS}/snakefile/rsid2chrom.yml -p -j 1 -c "qsub -X -V -d $TAG_DIR -q tagc -l nodes=1:ppn={threads} -e $TAG_DIR/stderr.log -o $TAG_DIR/stdout.log" -d $TAG_DIR -p
~~~

POSITIVE 

~~~
export CHROM=$(cat $TAG_DIR/../chrom_list.txt)
export NBCHROM=$(python -c "import os; print(2*len(os.getenv('CHROM').split()))")
time snakemake -s ${TAGOOS}/snakefile/tag.yml -p -j 32 -c "qsub -X -V -d $TAG_DIR -q tagc -l nodes=1:ppn={threads} -e $TAG_DIR/stderr.log -o $TAG_DIR/stdout.log" -d $TAG_DIR --latency-wait 60 -pn
~~~

NEGATIVE

~~~
export TAG_DIR=$TAG_NEG_DIR
export LABEL=-1
export TAG_RSID=$TAG_NEG_RSID
#
export CHROM=$(seq 22)
time snakemake -s ${TAGOOS}/snakefile/tag.yml -p -j 32 -c "qsub -X -V -d $TAG_DIR -q tagc -l nodes=1:ppn={threads} -e $TAG_DIR/stderr.log -o $TAG_DIR/stdout.log" -d $TAG_DIR --latency-wait 60 -pn
~~~

MODEL

First get chroms as a function of AUCs

~~~
export CHROM=$(cat $TAG_POS_DIR/../chrom_list.txt)
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_model1
#
time snakemake -s ${TAGOOS}/snakefile/model.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

~~~
find $OUTDIR/CV/. -name auc.txt |sort |while read F; do AUC=$(cat $F); F2=${F%"/auc.txt"}; CHROM=$(echo ${F2##*/}); echo $CHROM $AUC ;done |sort -k2,2nr |grep -v nan |awk -v OUTDIR="$OUTDIR" '{print $0>OUTDIR"/CV/chrom_aucs.txt";if($2>=0.6){print $1>OUTDIR"/CV/selected_chroms.txt"}}'
~~~

If AUCs of chroms not good, then create a new model for this chromosomes

~~~
export CHROM=$(cat $PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_model1/CV/selected_chroms.txt)
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_model2
#
time snakemake -s ${TAGOOS}/snakefile/model.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

Score DBSNP

~~~
export THREADS=8
export CHROM=$(seq 22)
#export CHROM=$(cat $PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_model1/CV/selected_chroms.txt)
export MODEL_PKL=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_model1/model.pkl
#
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export SCRIPT_DIR=${TAGOOS}/script
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_dbsnp

time snakemake -s ${TAGOOS}/snakefile/score.yml -j 32 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

