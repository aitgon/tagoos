# Variant  processing and annotation

Region variables

~~~
export REGION=intronic
export GENOMIC_REGION_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/hg19_5utrExonIntron3utrExon.bed
~~~

~~~
export REGION=intergenic
export GENOMIC_REGION_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_RefSeqGenes_intergenic_subtract_upstream1000.bed
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
export CHROM_SIZES=${HOME}/MEGA/2015_svmgwas/analysis/170412_genome_regions/raw_hg19.chrom.sizes
export REFGENE=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/raw_ucsc_hg19_RefSeqGenes_gene.bed
sort -k1,1 -k2,2n ${REFGENE} -o ${REFGENE}
export LD=0.8
export THREADS=16 # default 8
export SNAKEMAKE_J=32
export QUEUE=batch # default batch
~~~

# NCBI GRASP SNPs

## Download (Region-independent) and process from here

- https://s3.amazonaws.com/NHLBI_Public/GRASP/GraspFullDataset2.zip

~~~
time snakemake -s ${TAGOOS}/snakefile/04data_snp/01grasp_download.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $GRASP_DATA_DIR/stderr.log -o $GRASP_DATA_DIR/stdout.log" -d $GRASP_DATA_DIR -pn
~~~

## Process (Region-dependent)

~~~
time snakemake -s ${TAGOOS}/snakefile/04data_snp/02grasp_region.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $GRASP_DATA_DIR/stderr.log -o $GRASP_DATA_DIR/stdout.log" -d $GRASP_DATA_DIR -pn
~~~

# Download dbSNP (necessary for 1000 genomes) (Region-independent)

~~~
export CHROM="$(seq 1 22)"
export URL_DBSNP=ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b150_GRCh37p13/BED/bed_chr_{chr}.bed.gz

time snakemake -s ${TAGOOS}/snakefile/04data_snp/03dbsnp_download.yml -j 48 --keep-going --rerun-incomplete -c "qsub -X -V -d $PWD -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $DBSNP_DIR/stderr.log -o $DBSNP_DIR/stdout.log" -d $DBSNP_DIR -pn
~~~

# Download 1000 genomes (Region-independent) and filter EUR pop

~~~
export CHROM="$(seq 22)"
export URL_GENOME1K_SOMATIC="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chr{chr}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"
#export URL_GENOME1K_X="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.vcf.gz"
#export URL_GENOME1K_Y="ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.vcf.gz"
time snakemake -s ${TAGOOS}/snakefile/04data_snp/04genome1k_download.yml -p -j $SNAKEMAKE_J --keep-going --rerun-incomplete -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads},walltime=48:00:00 -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR --latency-wait 60 -pn
~~~

# Process 1000 Genomes

## Filter region and convert to plink and peak bed (Region-dependent) using these inputs:

- Genomic region: $HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/hg19_5utrExonIntron3utrExon.bed
- Peak beds: out/data/snp/1000genomes/peak_bed/1/chr1_peak.bed

~~~
export GENOME1K_DIR=$PWD/out/data/snp/1000genomes
export CHROM="$(seq 22)"
export OUTDIR=$GENOME1K_DIR/${REGION}
time snakemake -s ${TAGOOS}/snakefile/04data_snp/05genome1k_region.yml -p -j $SNAKEMAKE_J --keep-going --rerun-incomplete -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads} -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

## Correlated and index variants of 1000 genome data (Region-dependent) with inputs:

~~~
# Inputs
export CHROM="$(seq 1 22)"
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/$REGION/plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
# Outputs to 
export OUTDIR=${GENOME1K_DIR}/${REGION}
time snakemake -s ${TAGOOS}/snakefile/04data_snp/06genome1k_ld_index.yml -p -j 256 --keep-going --rerun-incomplete -c "qsub -X -V -q $QUEUE -l nodes=1:ppn={threads},walltime=48:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

Then outputs to

- ${GENOME1K_DIR}/${REGION}/index3
- ${GENOME1K_DIR}/${REGION}/ld08

## Intersect/annotate the 1000 genome variants (Region-dependent)

This snakefile (data_snp/07annotate.yml) takes 1000 genomes SNPs (EUR and intronic/intergenic) and annotate them with _mergedannot_ to TSV and LIBSVM files

~~~
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export CHROM="$(seq 1 22)"
export SNP_DIR_IN=$PWD/out/data/snp/1000genomes/$REGION/peak_bed
export SNP_DIR_OUT=$PWD/out/data/snp/1000genomes/$REGION/peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/04data_snp/07annotate.yml -j 256 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $SNP_DIR_OUT/stderr.log -o $SNP_DIR_OUT/stdout.log" -d $SNP_DIR_OUT -pn
~~~

Then outputs to 

~~~
$ ls /cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/171028/out/data/snp/1000genomes/intronic/peak_bed/1/mergedannot/
annotation.libsvm  instance.txt  intersect.tsv  nonsorted_intersect.tsv
~~~

# INDEX (Region-dependent) (PROBABLY TRASH)

This snakefile takes the index SNPs and EUR LD relationships and will merge/join them to later aggregate annotations

~~~
#export INDEX_DIR=$PWD/out/${INDEX_LABEL}
export INDEX_DIR=$PWD/out/data/snp/1000genomes/${REGION}/index3
#time snakemake -s ${TAGOOS}/snakefile/04data_snp/08indexld_TRASH.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -d $INDEX_DIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $INDEX_DIR/stderr.log -o $INDEX_DIR/stdout.log" -d $INDEX_DIR --latency-wait 60 -pn
~~~

Then outputs to 

~~~
$ ls /cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/171028/out/data/snp/1000genomes/intronic/index3/chrom/1/chr1_index3.prune.in
/cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/171028/out/data/snp/1000genomes/intronic/index3/chrom/1/chr1_index3.prune.in
~~~

# Process DBSNP (NECESSARY?, NOT RUNNING FOR NOW) (PROBABLY TRASH)

Filter region dbsnp (region-dependent)

~~~
export CHROM="$(seq 1 22)"
export DBSNP_IN_DIR=$DBSNP_DIR
export DBSNP_OUT_DIR=$PWD/out/data/snp/dbsnp/${REGION}
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export THREADS=16
export QUEUE=batch # default batch#
time snakemake -s ${TAGOOS}/snakefile/04data_snp/09dbsnp_region_TRASH.yml -j 48 --keep-going --rerun-incomplete -c "qsub -X -V -d $PWD -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e stderr.log -o stdout.log" -d $PWD -pn
~~~



