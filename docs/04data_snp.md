# Variant  processing and annotation

Region variables

~~~
export REGION=intronic
export GENOMIC_REGION_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/hg19_5utrExonIntron3utrExon.bed
~~~

~~~
export REGION=intergenic
export GENOMIC_REGION_BED=$HOME/data/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_RefSeqGenes_intergenic_subtract_upstream1000.bed
~~~

Data folders

~~~
export ANNOT_LABEL=mergedannot
export DBSNP_DIR=$PWD/out/data/snp/dbsnp
export GENOME1K_DIR=$PWD/out/data/snp/1000genomes
export GRASP_DATA_DIR=$PWD/out/data/snp/grasp
export ANNOTATION_DIR=$PWD/out/data/annotation/${ANNOT_LABEL}
export INDEX_DIR=${GENOME1K_DIR}/${REGION}/index3
export INDEX_LD_DIR=${GENOME1K_DIR}/${REGION}/index3_ld
export LD_DIR=${GENOME1K_DIR}/${REGION}/ld08
~~~

Other variables

~~~
export CHROM_SIZES=${HOME}/data/2015_svmgwas/analysis/170412_genome_regions/raw_hg19.chrom.sizes
export REFGENE=$HOME/data/2015_svmgwas/analysis/170412_genome_regions/raw_ucsc_hg19_RefSeqGenes_gene.bed
export LD=0.8
export THREADS=16 # default 8
export SNAKEMAKE_J=32
export QUEUE=batch # default batch
~~~

# NCBI GRASP SNPs

Download (Region-independent)

~~~
time snakemake -s ${TAGOOS}/snakefile/data_snp/grasp_download.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $GRASP_DATA_DIR/stderr.log -o $GRASP_DATA_DIR/stdout.log" -d $GRASP_DATA_DIR -pn
~~~

Process (Region-dependent)

~~~
time snakemake -s ${TAGOOS}/snakefile/data_snp/grasp_region.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $GRASP_DATA_DIR/stderr.log -o $GRASP_DATA_DIR/stdout.log" -d $GRASP_DATA_DIR -pn
~~~

# Download dbSNP (necessary for 1000 genomes) and 1000 Genomes

dbSNP (Region-independent)

~~~
export CHROM="$(seq 1 22)"
export URL_DBSNP=ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b150_GRCh37p13/BED/bed_chr_{chr}.bed.gz

time snakemake -s ${TAGOOS}/snakefile/data_snp/dbsnp_download.yml -j 48 --keep-going --rerun-incomplete -c "qsub -X -V -d $PWD -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $DBSNP_DIR/stderr.log -o $DBSNP_DIR/stdout.log" -d $DBSNP_DIR -pn
~~~

Download 1000 genomes (Region-independent)


~~~
export CHROM="$(seq 22)"
export URL_GENOME1K_SOMATIC="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chr{chr}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
#export URL_GENOME1K_X="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.vcf.gz"
#export URL_GENOME1K_Y="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.vcf.gz"
time snakemake -s ${TAGOOS}/snakefile/data_snp/genome1k_download.yml -p -j $SNAKEMAKE_J --keep-going --rerun-incomplete -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads},walltime=48:00:00 -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR --latency-wait 60 -pn
~~~

# Process 1000 Genomes

Filter region and convert to plink and peak bed (Region-dependent)

~~~
export GENOME1K_DIR=$PWD/out/data/snp/1000genomes
export CHROM="$(seq 22)"
export OUTDIR=$GENOME1K_DIR/${REGION}
time snakemake -s ${TAGOOS}/snakefile/data_snp/genome1k_region.yml -p -j $SNAKEMAKE_J --keep-going --rerun-incomplete -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

Correlated and index variants of 1000 genome data (Region-dependent)

~~~
export CHROM="$(seq 1 22)"
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/$REGION/plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export OUTDIR=${GENOME1K_DIR}/${REGION}
time snakemake -s ${TAGOOS}/snakefile/data_snp/genome1k_ld_index.yml -p -j 256 --keep-going --rerun-incomplete -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads},walltime=48:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

Intersect/annotate the 1000 genome variants (Region-dependent)

~~~
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export CHROM="$(seq 1 22)"
export SNP_DIR_IN=$PWD/out/data/snp/1000genomes/$REGION/peak_bed
export SNP_DIR_OUT=$PWD/out/data/snp/1000genomes/$REGION/peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/data_snp/annotate.yml -j 256 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $SNP_DIR_OUT/stderr.log -o $SNP_DIR_OUT/stdout.log" -d $SNP_DIR_OUT -pn
~~~

TRASH??? INDEX (Region-dependent) TRASH???
Create index

~~~
#export INDEX_DIR=$PWD/out/${INDEX_LABEL}
export INDEX_DIR=$PWD/out/data/snp/1000genomes/${REGION}/index3
time snakemake -s ${TAGOOS}/snakefile/data_snp/indexld.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -d $INDEX_DIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $INDEX_DIR/stderr.log -o $INDEX_DIR/stdout.log" -d $INDEX_DIR --latency-wait 60 -pn
~~~

# Process DBSNP

Filter region dbsnp (region-dependent)

~~~
export CHROM="$(seq 1 22)"
export DBSNP_IN_DIR=$DBSNP_DIR
export DBSNP_OUT_DIR=$PWD/out/data/snp/dbsnp/${REGION}
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export THREADS=16
export QUEUE=batch # default batch
time snakemake -s ${TAGOOS}/snakefile/data_snp/dbsnp_region.yml -j 48 --keep-going --rerun-incomplete -c "qsub -X -V -d $PWD -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e stderr.log -o stdout.log" -d $PWD -pn
~~~



