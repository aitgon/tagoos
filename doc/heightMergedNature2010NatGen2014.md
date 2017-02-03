# heightMergedNature2010NatGen2014.rsid, 1kg1000000.rsid, annotation, index3

~~~
export TAG_RSID_POS=/cobelix/gonzalez/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg1000000
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
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# heightMergedNature2010NatGen2014.rsid, 1kg100000.rsid, annotation, index3

~~~
export TAG_RSID_POS=/cobelix/gonzalez/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export POS_LABEL=heightMergedNature2010NatGen2014
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
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# heightMergedNature2010NatGen2014.rsid, 1kg10000.rsid, annotation, index3

~~~
export TAG_RSID_POS=/cobelix/gonzalez/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg10000
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
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# heightMergedNature2010NatGen2014.rsid, 1kg3000.rsid, annotation, index3

~~~
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg3000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export OUTDIR=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export POSDIR=$PWD/out/${POS_LABEL}/pos/${ANNOT_LABEL}_${INDEX_LABEL}
export NEGDIR=$PWD/out/neg/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_POS=/cobelix/gonzalez/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eurchr
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# heightMergedNature2010NatGen2014.rsid, 1kg1000.rsid, annotation, index2

~~~
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg1000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index2
#
export OUTDIR=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export POSDIR=$PWD/out/${POS_LABEL}/pos/${ANNOT_LABEL}_${INDEX_LABEL}
export NEGDIR=$PWD/out/neg/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
export TAG_RSID_POS=/cobelix/gonzalez/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export TAG_RSID_NEG=$HOME/data/2015_svmgwas/data/variant/1000genomes/${NEG_LABEL}.rsid
export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $TAG_RSID_POS |cut -f1 |tr -d "chr" |sort -u -k1n)
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eurchr
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake.yml -p -j $NBCHROM -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

# Score nomaf

~~~
export RSID_LABEL=eurNoMaf
export RSID_PATH=${HOME}/data/2015_svmgwas/data/variant/1000genomes/eurNoMaf/eurNoMaf.rsid
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg3000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
#
export ANNOTATION_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}_1col.bed 
export GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eurNoMaf
export MODEL_PKL=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}/model.pkl
export VARIABLE=$PWD/out/${POS_LABEL}/${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}/variable.txt
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/svmgwas-appli4/script
export OUTDIR=$PWD/out/${POS_LABEL}/score_${RSID_LABEL}_${POS_LABEL}_${NEG_LABEL}_${ANNOT_LABEL}_${INDEX_LABEL}
#export CHROM=$($HOME/data/2015_svmgwas/data/hcomp/get_record  $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed.idx $HOME/data/2015_svmgwas/data/variant/1000genomes/eur/eur.peak.bed -f $RSID_PATH |cut -f1 |tr -d "chr" |sort -u -k1n)
export CHROM=$(seq 22)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s Snakemake_score.yml -j ${NBCHROM} -c "qsub -X -V -d $OUTDIR -q tagc -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -pn
# ? m
~~~

