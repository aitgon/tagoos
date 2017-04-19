

Download 1000 genome and convert to plink and peak bed

~~~
export REGION=genomic
#
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export CHROM=$(seq 1 22)
export THREADS=8
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/hg19.bed
export OUTDIR=$GENOME1K_DIR/${REGION}
time snakemake -s ${TAGOOS}/snakefile/download_genome1k.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Compute the correlated and index variants of 1000 genome data with the __genome1k.yml__ snakefile

~~~
export REGION=genomic
export LD=0.8
#
export CHROM=$(seq 1 22)
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/$REGION/plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export THREADS=2
export OUTDIR=${GENOME1K_DIR}/${REGION}
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/genome1k_ld_index.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Intersect/annotate the 1000 genome variants using the __annotate.yml__ snakefile

~~~
export ANNOT_LABEL=encode2
export REGION=genomic
export LD=0.8
#
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export CHROM=$(seq 1 22)
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/$REGION/peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/annotate.yml -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $SNP_DIR -pn
~~~

- Download the dbsnp variants using the __download_dbsnp.yml__ snakefile

~~~
export REGION=genomic
#
export CHROM=$(seq 1 22)
#export CHROM=22
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/UCSC_hg19_intronsUTRexons.bed
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export DBSNP_OUT_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export THREADS=2
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/download_dbsnp.yml -j $NBCHROM -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e stderr.log -o stdout.log" -d $PWD -pn
~~~

- Intersect/annotate dbsnp variants using the __annotate.yml__ snakefile

~~~
export ANNOT_LABEL=mergedannot
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export REGION=intronic
#
export CHROM=$(seq 22)
#export CHROM=22
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/annotate.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $SNP_DIR/stderr.log -o $SNP_DIR/stdout.log" -d $SNP_DIR -pn
~~~


