# Height, 1kg10000.rsid

~~~
export OUTDIR=$PWD/out_height_1kg10000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/Height_TITLE_Hundreds_of_variants.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg10000.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
# 17 m
~~~

