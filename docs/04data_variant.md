# Variant  processing and annotation

Region variables

~~~
export REGION=genomic
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/hg19.bed
~~~

~~~
export REGION=intronic
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/ucsc_hg19_RefSeqGenes_5utrExonIntron3utrExon.bed
~~~

~~~
export REGION=intergenprox
export GENOMIC_REGION_BED=${HOME}/MEGA/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_intergenic_proximal.bed
~~~

~~~
export REGION=intergendistal
export GENOMIC_REGION_BED=${HOME}/MEGA/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_intergenic_distal.bed
~~~

Other variables

~~~
export ANNOT_LABEL=mergedannot
export LD=0.8
export THREADS=16 # default 8
export SNAKEMAKE_J=32
export QUEUE=batch # default batch
export TAGOOS=${TAGOOS}
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
~~~

# NCBI GRASP SNPs

Download and process

~~~
export GRASP_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/grasp
time snakemake -s ${TAGOOS}/snakefile/data_variant/grasp.yml -p -j 16 -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads} -e $GRASP_DATA_DIR/stderr.log -o $GRASP_DATA_DIR/stdout.log" -d $GRASP_DATA_DIR -pn
~~~

# 1000 Genomes

Download 1000 genome and convert to plink and peak bed

Chrom 1-22 X Y

~~~
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export CHROM="$(seq 22) X Y"
export URL_GENOME1K_SOMATIC="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chr{chr}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
export URL_GENOME1K_X="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.vcf.gz"
export URL_GENOME1K_Y="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.vcf.gz"
time snakemake -s ${TAGOOS}/snakefile/data_variant/download_genome1k.yml -p -j $SNAKEMAKE_J -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR --latency-wait 60 -pn
~~~

~~~
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export CHROM="$(seq 22) X Y"
export OUTDIR=$GENOME1K_DIR/${REGION}
time snakemake -s ${TAGOOS}/snakefile/data_variant/genome1k_process_region.yml -p -j $SNAKEMAKE_J -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

Correlated and index variants of 1000 genome data

~~~
export CHROM="$(seq 1 22) X Y"
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/$REGION/plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export OUTDIR=${GENOME1K_DIR}/${REGION}
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/data_variant/genome1k_ld_index.yml -p -j $NBCHROM -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

Intersect/annotate the 1000 genome variants

~~~
export ANNOTATION_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}
export CHROM="$(seq 1 22) X Y"
export SNP_OUTDIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/$REGION/peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/data_variant/annotate.yml -j $SNAKEMAKE_J -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads} -e $SNP_OUTDIR/stderr.log -o $SNP_OUTDIR/stdout.log" -d $SNP_OUTDIR -pn
~~~

# DBSNP

Download the dbsnp variants

~~~
export CHROM="$(seq 1 22) X Y"
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export THREADS=16
export QUEUE=batch # default batch
time snakemake -s ${TAGOOS}/snakefile/data_variant/dbsnp_download.yml -j 48 -c "qsub -X -V -d $PWD -q ${QUEUE} -l nodes=1:ppn={threads} -e $DBSNP_DIR/stderr.log -o $DBSNP_DIR/stdout.log" -d $DBSNP_DIR -pn
~~~

Filter region dbsnp

~~~
export CHROM="$(seq 1 22) X Y"
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export DBSNP_OUT_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}
export THREADS=16
export QUEUE=batch # default batch
time snakemake -s ${TAGOOS}/snakefile/data_variant/dbsnp_region_filter.yml -j 48 -c "qsub -X -V -d $PWD -q ${QUEUE} -l nodes=1:ppn={threads} -e stderr.log -o stdout.log" -d $PWD -pn
~~~


Annotate dbsnp variants

~~~
export ANNOTATION_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}
export CHROM="$(seq 1 22) X Y"
export SNP_OUTDIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${REGION}
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/data_variant/annotate.yml -p -j $SNAKEMAKE_J -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads} -e $SNP_OUTDIR/stderr.log -o $SNP_OUTDIR/stdout.log" -d $SNP_OUTDIR -pn
~~~


