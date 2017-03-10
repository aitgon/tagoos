Split the annotation in different chromosomes using the __split_annotation.yml__ snakefile

~~~
export ANNOT_LABEL=annotationcorr
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export ANNOT_1COL_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}
#
export CHROM=$(seq 1 22)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/split_annotation.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ANNOT_1COL_DIR/stderr.log -o $ANNOT_1COL_DIR/stdout.log" -d $ANNOT_1COL_DIR -pn
~~~

Download 1000 genome and convert to plink and peak bed

~~~
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export CHROM=$(seq 1 22)
#export CHROM=1
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/download_genome1k.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Compute the correlated and index variants of 1000 genome data with the __genome1k.yml__ snakefile

~~~
export LD=0.8
export CHROM=$(seq 1 22)
#export CHROM=1
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
export GENOME1K_PLINKBED_DIR=$GENOME1K_DIR/intergenic_plink_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export THREADS=8
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/genome1k_ld_index.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GENOME1K_DIR/stderr.log -o $GENOME1K_DIR/stdout.log" -d $GENOME1K_DIR -pn
~~~

Intersect/annotate the 1000 genome variants using the __preannotate.yml__ snakefile

~~~
export ANNOT_LABEL=annotationcorr
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
#
export CHROM=$(seq 1 22)
#export CHROM=22
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/intergenic_peak_bed
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/preannotate.yml -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e tmp/stderr.log -o tmp/stdout.log" -d $SNP_DIR -pn
~~~

- Download the dbsnp variants using the __download_dbsnp.yml__ snakefile

~~~
export CHROM=$(seq 1 22)
#export CHROM=22
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export THREADS=8
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/download_dbsnp.yml -j $NBCHROM -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e stderr.log -o stdout.log" -d $PWD -pn
~~~

- Intersect/annotate dbsnp variants using the __preannotate.yml__ snakefile

~~~
export ANNOT_LABEL=annotationcorr
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
#
export CHROM=$(seq 1 22)
#export CHROM=22
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s ${TAGOOS}/snakefile/preannotate.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $SNP_DIR/stderr.log -o $SNP_DIR/stdout.log" -d $SNP_DIR -pn
~~~

