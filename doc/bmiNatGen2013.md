# bmiNatGen2013.rsid, 1kg100000.rsid, annotation

~~~
export TAG_RSID_POS=$HOME/MEGA/2015_svmgwas/data/variant/literature_association/traits/bmiNatGen2013.rsid
export POS_LABEL=bmiNatGen2013
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export POSDIR=$PWD/out/${POS_LABEL}/pos/${ANNOT_LABEL}_${INDEX_LABEL}
export NEGDIR=$PWD/out/neg/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eurchr
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

