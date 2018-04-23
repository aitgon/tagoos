Region variables

$REGION \in {'intronic', 'intergenic'}$

~~~
export REGION=intronic # default intronic
export GENOMIC_REGION_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/hg19_5utrExonIntron3utrExon.bed
~~~

~~~
export REGION=intergenic
export GENOMIC_REGION_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_RefSeqGenes_intergenic.bed
~~~

~~~
export QUEUE=batch
export THREADS=16
export PYTHONBIN=$(which python)
~~~

~~~
export POS_LABEL=GRASP108
export NEG_LABEL=1kg1000000
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
~~~

~~~
export CHROM_SIZES=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/raw_hg19.chrom.sizes
~~~

~~~
export TAGOOS=${HOME}/Software/repositories/tagoos
export TAGOOS_APPLI=${HOME}/Data/2015_svmgwas/repositories/tagoos-appli
~~~

# Predict

Make window (Region-independent)

_Algo_

- Create 30000000 long windows

~~~
export GWINDOW_LENGTH=30000000
export OUTDIR=$PWD/out/data/snp/gwindow
export GENOME_WINDOW_BED=${OUTDIR}/genome_splitted.bed
if [ ! -f $GENOME_WINDOW_BED ]; 
then mkdir -p ${OUTDIR} && bedtools makewindows -g ${CHROM_SIZES} -w $GWINDOW_LENGTH |uniq  |awk '{print $1"\t"$2"\t"$3"\t"$1":"$2+1"-"$3}' |sort -k1,1 -k2,2n -k3,3n |grep -P "chr[0-9][0-9]?" > $GENOME_WINDOW_BED
fi
export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED | sort| grep "chr1:" |head -n1)
export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED | sort)
time snakemake -s ${TAGOOS}/snakefile/06predict/01makewindow.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d ${OUTDIR} -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d ${OUTDIR} --latency-wait 60 -pn
~~~

_Algo_

- Make single nucleotide peaks for 30000000 windows
- Intersect single nucleotide peaks with regions

Annotate (Region-dependent)

~~~
export GWINDOW_DIR=$PWD/out/data/snp/gwindow
export OUTDIR=$PWD/out/${REGION}/predict
time snakemake -s ${TAGOOS}/snakefile/06predict/02region.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" --latency-wait 60 -d $OUTDIR -pn
~~~

- Annotate region single nucleotide peaks using selected features from models
- Collapse different annotation of single nucleotide
- Collapse single nucleotides with same annotation combinations

~~~
export ANNOTATION_BED=${PWD}/out/${REGION}/train/mergedannot_selected.bed
export MAX_ANNOTATION_ID=$(tail -n1 /cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/data/annotation/mergedannot/variableid2variable.tsv |cut -f 1);
export MODEL_BST=${PWD}/out/${REGION}/train/model.bst
time snakemake -s ${TAGOOS}/snakefile/06predict/03predict.yml -j 64 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -p  -k --rerun-incomplete --latency-wait 60 -n
~~~

# Calculate p-value from ecdf

_Algo_

- Create random genomic positions
- Intersect random genomic positions with region bed
- Intersect random regional positions with annotations
- Score annotatied random regional positions
- Calculate pval=1-ecdf

~~~
export RANDOM_BED=$PWD/out/data/snp/random.bed
if [ ! -f $RANDOM_BED ]; 
then mkdir -p ${OUTDIR} && bedtools random -seed 123 -n 10010000 -l 1 -g $CHROM_SIZES |cut -f1-3 |sort -k1,1 -k2,2n -k3,3n -u |shuf -n 10000000 |sort -k1,1 -k2,2n >$RANDOM_BED
fi 
~~~

~~~
export PREDICTION_BED=${PWD}/out/${REGION}/predict/prediction_annotation.bed
export RANDOM_BED=$PWD/out/data/snp/random.bed
export OUTDIR=$PWD/out/${REGION}/predict
time snakemake -s ${TAGOOS}/snakefile/06predict/04pval.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d ${OUTDIR} -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d ${OUTDIR} --latency-wait 60 -pn
~~~


