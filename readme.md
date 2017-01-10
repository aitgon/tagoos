# All, 1kg10000000.rsid
    
~~~ 
export OUTDIR=$PWD/out_1kg10000000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
#export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac_1col.bed
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
time snakemake -s Snakemake.yml -p -j ${NCORES} -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn=${NCORES} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
# ? min
~~~

# All, 1kg1000000.rsid
    
~~~ 
export OUTDIR=$PWD/out_1kg1000000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg1000000.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
# 200 min
~~~

# All, 1kg100000.rsid

~~~ 
export OUTDIR=$PWD/out_1kg100000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg100000.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
# 144 min
~~~

# All, 1kg10000.rsid

~~~
export OUTDIR=$PWD/out_1kg10000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg10000.rsid
export CHROM=$(seq 1 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
# 17 m
~~~

# Test, 1kg1000.rsid

~~~ 
export OUTDIR=$PWD/out_test
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108_10000.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/1kg10000.rsid
export CHROM=$(seq 20 22)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac_1col.bed
#export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -pn
~~~

