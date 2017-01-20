# serumUrate.rsid, 1kg10000.rsid, annotation

~~~
export POS_LABEL=serumUrate
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# serumUrate.rsid, 1kg100000.rsid, annotation

~~~
export POS_LABEL=serumUrate
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

