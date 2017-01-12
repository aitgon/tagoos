# All, 1kg10000000.rsid (does not work -> too large)
    
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
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
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
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# 144 min
~~~

# GRASP 108, 1kg1000000.rsid

~~~
export POS_LABEL=grasp108
export NEG=1kg1000000
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG}
mkdir -p $OUTDIR
cp -r $PWD/out/out_${NEG}/neg $OUTDIR/neg
rm -f $OUTDIR/neg/neg_index2annot_r2.tsv $OUTDIR/neg/neg_index2annot_r2_label.tsv
~~~

~~~
export POS_LABEL=grasp108
export NEG=1kg1000000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP 108, 1kg100000.rsid

~~~
export POS_LABEL=grasp108
export NEG=1kg100000
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG}
mkdir -p $OUTDIR
cp -r $PWD/out/out_${NEG}/neg $OUTDIR/neg
rm -f $OUTDIR/neg/neg_index2annot_r2.tsv $OUTDIR/neg/neg_index2annot_r2_label.tsv
~~~

~~~
export POS_LABEL=grasp108
export NEG=1kg100000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP 108, 1kg10000.rsid

~~~
export POS_LABEL=grasp108
export NEG=1kg10000
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG}
mkdir -p $OUTDIR
cp -r $PWD/out/out_${NEG}/neg $OUTDIR/neg
rm -f $OUTDIR/neg/neg_index2annot_r2.tsv $OUTDIR/neg/neg_index2annot_r2_label.tsv
~~~

~~~
export POS_LABEL=grasp108
export NEG=1kg10000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
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
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
~~~

