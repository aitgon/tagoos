# height.rsid, 1kg1000.rsid, annotation, index2

chr22

~~~
export RSID_LABEL=chr22
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index2
#
export MODEL_LABEL=${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
#
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/1000genomes/chr22/chr22.rsid
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${PWD}/out/out/out_${MODEL_LABEL}/model.pkl
export VARIABLE=${PWD}/out/out/out_${MODEL_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/out/outscore/outscore_${RSID_LABEL}_${MODEL_LABEL}
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

eur

~~~
export RSID_LABEL=eur
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/1000genomes/eur/eur.rsid
export POS_LABEL=height
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index2
#
export MODEL_LABEL=${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
#
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${PWD}/out/out/out_${MODEL_LABEL}/model.pkl
export VARIABLE=${PWD}/out/out/out_${MODEL_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/out/outscore/outscore_${RSID_LABEL}_${MODEL_LABEL}
#export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export CHROM=$(seq 22)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

