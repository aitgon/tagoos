# GRASP108_10000, 1kg1000.rsid, annotation, common_no_known_medical_impact

~~~
export RSID_LABEL=common_no_known_medical_impact
#
export POS_LABEL=GRASP108
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
export MODEL_LABEL=${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
#
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/clinvar/${RSID_LABEL}.rsid
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${PWD}/out/out_${MODEL_LABEL}/model.pkl
export VARIABLE=${PWD}/out/out_${MODEL_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/outscore/outscore_${RSID_LABEL}_${MODEL_LABEL}
#export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export CHROM=$(seq 22)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

# GRASP108_10000, 1kg1000.rsid, annotation, common_and_clinical

~~~
export RSID_LABEL=common_and_clinical
#
export POS_LABEL=GRASP108
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
export MODEL_LABEL=${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
#
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/clinvar/${RSID_LABEL}.rsid
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${PWD}/out/out_${MODEL_LABEL}/model.pkl
export VARIABLE=${PWD}/out/out_${MODEL_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/outscore/outscore_${RSID_LABEL}_${MODEL_LABEL}
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

# Test2: GRASP108_10000, 1kg1000.rsid, annotation, common_and_clinical_100

~~~
export RSID_LABEL=common_and_clinical_100
#
export POS_LABEL=GRASP108
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
export MODEL_LABEL=${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
#
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/clinvar/${RSID_LABEL}.rsid
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${PWD}/out/out_${MODEL_LABEL}/model.pkl
export VARIABLE=${PWD}/out/out_${MODEL_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/outscore/outscore_${RSID_LABEL}_${MODEL_LABEL}
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

# Test: GRASP108_10000, 1kg1000.rsid, youngh3k27ac, common_and_clinical

~~~
export RSID_LABEL=common_and_clinical
export MODEL_LABEL=GRASP108_10000_1kg10000
export ANNOT_LABEL=youngh3k27ac
#
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/clinvar/${RSID_LABEL}.rsid
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export MODEL_PKL=${PWD}/out/out_${MODEL_LABEL}_${ANNOT_LABEL}/model.pkl
export VARIABLE=${PWD}/out/out_${MODEL_LABEL}_${ANNOT_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/outscore/out_${RSID_LABEL}_${MODEL_LABEL}_${ANNOT_LABEL}
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

