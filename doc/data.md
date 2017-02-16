# Download dbsnp

~~~
export CHROM=$(seq 1 22)
export DBSNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s snakefile/download_dbsnp.yml -j $NBCHROM -c "qsub -X -V -d $PWD -q tagc -l nodes=1:ppn={threads} -e stderr.log -o stdout.log" -d $PWD -pn
~~~

# Split annotation

~~~
export ANNOT_LABEL=annotationcorr
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export ANNOT_1COL_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}
#
export CHROM=$(seq 1 22)
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s snakefile/split_annotation.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ANNOT_1COL_DIR/stderr.log -o $ANNOT_1COL_DIR/stdout.log" -d $ANNOT_1COL_DIR -pn
~~~

# dbsnp

~~~
export ANNOT_LABEL=annotationcorr
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
#
export CHROM=$(seq 1 22)
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/dbsnp
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s snakefile/preannotate.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $SNP_DIR/stderr.log -o $SNP_DIR/stdout.log" -d $SNP_DIR -pn
~~~

# genome1k

Intersect genome1k with annotatecorr

~~~
export ANNOT_LABEL=annotationcorr
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
#
export CHROM=$(seq 1 22)
export SNP_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eur
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s snakefile/preannotate.yml -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e tmp/stderr.log -o tmp/stdout.log" -d $SNP_DIR annotated_tsv -pn
~~~

1k genome plink bed and peak bed

~~~
export CHROM=$(seq 21 22)
export GENOME1K_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes/eur
export SCRIPTDIR=$HOME/data/2015_svmgwas/repositories/tagoos/script
export NBCHROM=`python -c "import os; print(len(os.getenv('CHROM').split()))"`
time snakemake -s genome1k.yml -p -j $NBCHROM -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e tmp/stderr.log -o tmp/stdout.log" -d $GENOME1K_DIR -pn
~~~

