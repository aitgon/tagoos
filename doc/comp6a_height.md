# height.rsid, 1kg10000.rsid, annotation

~~~
export POS_LABEL=height
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# height.rsid, 1kg1000.rsid, annotation, index1

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_POS=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# height.rsid, 1kg1000.rsid, annotation, index2

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index2
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_POS=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# height.rsid, 1kg1000.rsid, annotation, index3

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_POS=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# height.rsid, 1kg100000.rsid, annotation

~~~
export POS_LABEL=height
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# height.rsid, 1kg10000.rsid, annotation, Model and test with chrom 1

Create wdir and Filter test (1) chrom

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}_chr1
export TAG_RSID_POS_RAW=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/${POS_LABEL}.rsid
export TAG_RSID_POS=$OUTDIR/tag_rsid_pos_deltaChr1.rsid
export TEST_TAG=$OUTDIR/tag_rsid_pos_chr1.rsid
#
mkdir -p ${OUTDIR}
$HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS_RAW |grep -v -w chr1 |cut -f4 >$TAG_RSID_POS
$HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS_RAW |grep -w chr1 |cut -f4 >$TEST_TAG
#
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

Test model (Height tags, chrom 1)

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}_chr1
export TEST_TAG=$OUTDIR/tag_rsid_pos_chr1.rsid
#
# Given test variants -> get all LD variants
export RSID_PATH=$OUTDIR/test_tag_ld.rsid
/cobelix/gonzalez/data/2015_svmgwas/data/hcomp/get_record /cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr1/chr1_ld.ld.f3.idx /cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr1/chr1_ld.ld -f $TEST_TAG |cut -f6 | sort -u >$RSID_PATH
#
# Predict with model
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${OUTDIR}/model.pkl
export VARIABLE=${OUTDIR}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export CHROM=1
export NBCHROM=1
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
mv $OUTDIR/score.tsv $OUTDIR/score_height_chrom1.tsv 
~~~

Test model (Height Grasp Model, chrom 1)

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}_chr1
export TEST_TAG=$OUTDIR/tag_rsid_pos_chr1.rsid
#
# Given test variants -> get all LD variants
export RSID_PATH=$OUTDIR/test_tag_ld.rsid
/cobelix/gonzalez/data/2015_svmgwas/data/hcomp/get_record /cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr1/chr1_ld.ld.f3.idx /cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr1/chr1_ld.ld -f $TEST_TAG |cut -f6 | sort -u >$RSID_PATH
#
# Predict with model
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${HOME}/data/2015_svmgwas/repositories/svmgwas-appli4/out/out/out_serumUrate_1kg10000_annotation/model.pkl
export VARIABLE=${HOME}/data/2015_svmgwas/repositories/svmgwas-appli4/out/out/out_serumUrate_1kg10000_annotation/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export CHROM=1
export NBCHROM=1
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
mv $OUTDIR/score.tsv $OUTDIR/score_height_chrom1.tsv 
~~~

Test model (Serum urate tags, chrom 1)

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}_chr1
export TAG_RSID_POS_RAW=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/serumUrate.rsid
export TEST_TAG=$OUTDIR/tag_rsid_serumUrate_chr1.rsid
#
$HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS_RAW |grep -w chr1 |cut -f4 >$TEST_TAG
~~~

~~~
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}_chr1
export TEST_TAG=$OUTDIR/tag_rsid_serumUrate_chr1.rsid
#
# Given test variants -> get all LD variants
export RSID_PATH=$OUTDIR/test_tag_ld.rsid
/cobelix/gonzalez/data/2015_svmgwas/data/hcomp/get_record /cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr1/chr1_ld.ld.f3.idx /cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr1/chr1_ld.ld -f $TEST_TAG |cut -f6 | sort -u >$RSID_PATH
#
# Predict with model
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${OUTDIR}/model.pkl
export VARIABLE=${OUTDIR}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export CHROM=1
export NBCHROM=1
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
mv $OUTDIR/score.tsv $OUTDIR/score_other_chrom1.tsv 
~~~


