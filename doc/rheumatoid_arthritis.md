# Rheumatoid_arthritis.rsid, neg Grasp108

~~~
export NEG=grasp108
export OUTDIR=$PWD/out/out_Rheumatoid_arthritis_${NEG}
mkdir -p $OUTDIR
cp -r $PWD/out/out_grasp108_1kg10000/pos $OUTDIR/neg
rm -f $OUTDIR/neg/*
~~~

~~~
export POS=Rheumatoid_arthritis
export OUTDIR=$PWD/out/out_${POS}_${NEG}
#mkdir -p $OUTDIR
cp -r $PWD/out/out_${POS}_1kg10000/pos $OUTDIR/pos
rm -f $OUTDIR/pos/*
~~~

~~~
export NEG=grasp108
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/Rheumatoid_arthritis.rsid
#
export OUTDIR=$PWD/out/out_Rheumatoid_arthritis_${NEG}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# Rheumatoid_arthritis.rsid, 1kg10000.rsid

~~~
export NEG=1kg10000
export OUTDIR=$PWD/out/out_Rheumatoid_arthritis_${NEG}
mkdir -p $OUTDIR
cp -r $PWD/out_${NEG}/neg $OUTDIR/neg
rm -f $OUTDIR/neg/neg_index2annot_r2.tsv $OUTDIR/neg/neg_index2annot_r2_label.tsv
~~~

~~~
export NEG=1kg10000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/Rheumatoid_arthritis.rsid
#
export OUTDIR=$PWD/out/out_Rheumatoid_arthritis_${NEG}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# Rheumatoid_arthritis.rsid, 1kg100000.rsid

~~~
export NEG=1kg100000
export OUTDIR=$PWD/out/out_Rheumatoid_arthritis_${NEG}
mkdir -p $OUTDIR
cp -r $PWD/out_${NEG}/neg $OUTDIR/neg
rm -f $OUTDIR/neg/neg_index2annot_r2.tsv $OUTDIR/neg/neg_index2annot_r2_label.tsv
~~~

~~~
export NEG=1kg100000
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/GRASP/Rheumatoid_arthritis.rsid
#
export OUTDIR=$PWD/out/out_Rheumatoid_arthritis_${NEG}
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/annotation_1col.bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
time snakemake -s Snakemake.yml -p -j 15 -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

