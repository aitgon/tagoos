# Score dbsnp

~~~
export RSID_LABEL=dbsnp
export POS_LABEL=GRASP108
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotationcorr
export INDEX_LABEL=index2
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
#
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export MODEL_PKL=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}/model.pkl
export VARIABLE=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export OUTDIR=$PWD/out/${POS_LABEL}/score_${RSID_LABEL}_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
#export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export CHROM=$(seq 1 22)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s snakefile/score_dbsnp.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP108.rsid, 1kg100000.rsid, annotationcorr, index2

~~~
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export POS_LABEL=GRASP108
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotationcorr
export INDEX_LABEL=index2
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
#
export OUTDIR=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export POSDIR=$PWD/out/${POS_LABEL}/pos/${ANNOT_LABEL}_${INDEX_LABEL}
export NEGDIR=$PWD/out/neg/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eur
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s snakefile/Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~
