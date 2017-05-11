# Variant  processing and annotation

General variables

Region and the region bed file can take one of these four values

~~~
export REGION=genomic
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/hg19.bed
~~~

~~~
export REGION=intronic
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/UCSC_hg19_intronsUTRexons.bed
~~~

~~~
export REGION=intergenprox
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/hg19_intergenic_proximal.bed
~~~

~~~
export REGION=intergendistal
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/hg19_intergenic_distal.bed
~~~

These are other variables

~~~
export ANNOT_LABEL=mergedannot
export LD=0.8
export THREADS=2
export SNAKEMAKE_J=32
~~~

# NCBI GRASP SNPs

Download and process

~~~
export GRASP_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/grasp
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/variant/grasp.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GRASP_DATA_DIR/stderr.log -o $GRASP_DATA_DIR/stdout.log" -d $GRASP_DATA_DIR -pn
~~~

# 1000 Genomes

Download 1000 genome and convert to plink and peak bed

~~~
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export CHROM=$(seq 1 22)
export OUTDIR=$GENOME1K_DIR/${REGION}
time snakemake -s ${TAGOOS}/snakefile/download_genome1k.yml -p -j $SNAKEMAKE_J -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Correlated and index variants of 1000 genome data

~~~
export CHROM=$(seq 22)
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/$REGION/plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export OUTDIR=${GENOME1K_DIR}/${REGION}
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/genome1k_ld_index.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Intersect/annotate the 1000 genome variants

~~~
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export CHROM=$(seq 22)
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/$REGION/peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/annotate.yml -j $SNAKEMAKE_J -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $SNP_DIR -pn
~~~

# DBSNP

- Download the dbsnp variants

~~~
export CHROM=$(seq 22)
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export DBSNP_OUT_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export THREADS=2
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/download_dbsnp.yml -j $NBCHROM -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e stderr.log -o stdout.log" -d $PWD -pn
~~~

- Intersect/annotate dbsnp variants

~~~
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export CHROM=$(seq 22)
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/annotate.yml -p -j $SNAKEMAKE_J -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $SNP_DIR/stderr.log -o $SNP_DIR/stdout.log" -d $SNP_DIR -pn
~~~


