All

~~~
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg10000.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
#export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac_1col.bed
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export OUTDIR=$PWD/out_eur
export NCORES=16
time snakemake -s Snakemake.yml -p -j ${NCORES} -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn=${NCORES} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
~~~
