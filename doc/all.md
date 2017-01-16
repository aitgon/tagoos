# GRASP102_123k, 1kg100000, annotation

~~~
export POS_LABEL=GRASP102_123k
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
mkdir -p $OUTDIR
#
cp -r ${HOME}/data/2015_svmgwas/repositories/svmgwas-appli4/out/out_GRASP108_${NEG_LABEL}_${ANNOT_LABEL}/neg $OUTDIR/
~~~

~~~
export POS_LABEL=GRASP102_123k
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP105_123k, 1kg100000, annotation

~~~
export POS_LABEL=GRASP105_123k
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
mkdir -p $OUTDIR
#
cp -r ${HOME}/data/2015_svmgwas/repositories/svmgwas-appli4/out/out_GRASP108_${NEG_LABEL}_${ANNOT_LABEL}/neg $OUTDIR/
~~~

~~~
export POS_LABEL=GRASP105_123k
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP108, 1kg100000, annotation

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
mkdir -p $OUTDIR
#
cp -r $PWD/out/out_GRASP108_1kg10000_${ANNOT_LABEL}/pos $OUTDIR/pos
~~~

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP108, 1kg100000_2, annotation

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg100000_2
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
mkdir -p $OUTDIR
#
cp -r $PWD/out/out_GRASP108_1kg10000_${ANNOT_LABEL}/pos $OUTDIR/pos
~~~

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg100000_2
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# GRASP108, 1kg10000, annotation

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
mkdir -p $OUTDIR
~~~

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# Test: GRASP108_10000, 1kg1000.rsid, youngh3k27ac

~~~
export POS_LABEL=GRASP108_10000
export NEG_LABEL=1kg10000
export ANNOT_LABEL=youngh3k27ac
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
mkdir -p $OUTDIR
~~~

~~~
export POS_LABEL=GRASP108_10000
export NEG_LABEL=1kg10000
export ANNOT_LABEL=youngh3k27ac
#
export OUTDIR=$PWD/out/out_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/${POS_LABEL}.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

