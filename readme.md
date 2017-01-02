Positive

~~~
export TAG_RSID=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac_1col.bed
export OUTDIR=$PWD/out_eur
snakemake -s Snakemake.yml -np
~~~
