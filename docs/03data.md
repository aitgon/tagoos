# Download and process annotations

Encode2 download and process

~~~
export ENCODE2_URL="https://www.encodeproject.org/report.tsv?type=Experiment&replicates.library.biosample.donor.organism.scientific_name=Homo+sapiens&assembly=hg19&assay_title=ChIP-seq&assay_title=DNase-seq&assay_title=FAIRE-seq&assay_slims=DNA+accessibility&assay_slims=DNA+binding&files.file_type=bed+narrowPeak&field=%40id&field=accession&field=assay_term_name&field=assay_title&field=target.label&field=target.gene_name&field=biosample_summary&field=biosample_term_name&field=description&field=lab.title&field=award.project&field=status&field=replicates.biological_replicate_number&field=replicates.technical_replicate_number&field=replicates.antibody.accession&field=replicates.library.biosample.organism.scientific_name&field=replicates.library.biosample.life_stage&field=replicates.library.biosample.age&field=replicates.library.biosample.age_units&field=replicates.library.biosample.treatments.treatment_term_name&field=replicates.library.biosample.treatments.treatment_term_id&field=replicates.library.biosample.treatments.concentration&field=replicates.library.biosample.treatments.concentration_units&field=replicates.library.biosample.treatments.duration&field=replicates.library.biosample.treatments.duration_units&field=replicates.library.biosample.synchronization&field=replicates.library.biosample.post_synchronization_time&field=replicates.library.biosample.post_synchronization_time_units&field=replicates.%40id&field=files"
export ENCODE2_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/encode2
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/encode2.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ENCODE2_DATA_DIR/stderr.log -o $ENCODE2_DATA_DIR/stdout.log" -d $ENCODE2_DATA_DIR -pn
~~~

Roadmap download and process

~~~
export ROADMAP_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/roadmap
export ROADMAP_URL_LIST=${TAGOOS}/data/roadmap_url_list.txt
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/roadmap.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ROADMAP_DATA_DIR/stderr.log -o $ROADMAP_DATA_DIR/stdout.log" -d $ROADMAP_DATA_DIR -pn
~~~

Merge annotations

~~~
export ANNOTATION_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based
time snakemake -s ${TAGOOS}/snakefile/annotation/merge_annotations.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ENCODE2_DATA_DIR/stderr.log -o $ANNOTATION_DIR/stdout.log" -d $ANNOTATION_DIR -pn
~~~

Split annotations by chromosoms

~~~
export ANNOT_LABEL=mergedannot
export ANNOTATION_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based
#
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export ANNOT_1COL_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}
#
export CHROM=$(seq 1 22)
export THREADS=2
time snakemake -s ${TAGOOS}/snakefile/annotation/split_annotation.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ANNOT_1COL_DIR/stderr.log -o $ANNOT_1COL_DIR/stdout.log" -d $ANNOT_1COL_DIR -pn
~~~

Download 1000 genome and convert to plink and peak bed

~~~
export VARIANT_POSITION=intronic
#
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export CHROM=$(seq 1 22)
export THREADS=8
#export REFGENE_BED=$HOME/data/2015_svmgwas/data/var/hg19.refGene.bed
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/UCSC_hg19_intronsUTRexons.bed
export GENOME1K_OUT_DIR=$GENOME1K_DIR/$VARIANT_POSITION
time snakemake -s ${TAGOOS}/snakefile/download_genome1k.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Compute the correlated and index variants of 1000 genome data with the __genome1k.yml__ snakefile

~~~
export VARIANT_POSITION=intronic
export LD=0.8
#
export CHROM=$(seq 1 22)
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/$VARIANT_POSITION/plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export THREADS=8
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/genome1k_ld_index.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Intersect/annotate the 1000 genome variants using the __preannotate.yml__ snakefile

~~~
export ANNOT_LABEL=mergedannot
export VARIANT_POSITION=intronic
export LD=0.8
#
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export CHROM=$(seq 1 22)
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/$VARIANT_POSITION/peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/preannotate.yml -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $SNP_DIR -pn
~~~

- Download the dbsnp variants using the __download_dbsnp.yml__ snakefile

~~~
export VARIANT_POSITION=intronic
#
export CHROM=$(seq 1 22)
#export CHROM=22
export GENOMIC_REGION_BED=${HOME}/data/2015_svmgwas/data/var/genome_regions/UCSC_hg19_intronsUTRexons.bed
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export DBSNP_OUT_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${VARIANT_POSITION}
export THREADS=4
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/download_dbsnp.yml -j $NBCHROM -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e stderr.log -o stdout.log" -d $PWD -pn
~~~

- Intersect/annotate dbsnp variants using the __preannotate.yml__ snakefile

~~~
export ANNOT_LABEL=mergedannot
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export VARIANT_POSITION=intronic
#
export CHROM=$(seq 1 22)
#export CHROM=22
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp/${VARIANT_POSITION}
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
time snakemake -s ${TAGOOS}/snakefile/preannotate.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $SNP_DIR/stderr.log -o $SNP_DIR/stdout.log" -d $SNP_DIR -pn
~~~

