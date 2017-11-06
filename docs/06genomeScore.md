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
export TAGOOS_APPLI=${HOME}/data/2015_svmgwas/repositories/tagoos-appli
~~~

# Random and p-value from ecdf

_Algo_

- Create random genomic positions
- Intersect random genomic positions with region bed
- Intersect random regional positions with annotations
- Score annotatied random regional positions
- Calculate pval=1-ecdf

~~~
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/annotation/${ANNOT_LABEL}.bed
export MODEL_PKL=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}/model.pkl
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/genome_score
export RANDOM_BED=$PWD/out/data/snp/random.bed
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
if [ ! -f $RANDOM_BED ]; 
then mkdir -p ${OUTDIR} && bedtools random -seed 123 -n 10010000 -l 1 -g $CHROM_SIZES |cut -f1-3 |sort -k1,1 -k2,2n -k3,3n -u |shuf -n 10000000 |sort -k1,1 -k2,2n >$RANDOM_BED
fi
time snakemake -s ${TAGOOS}/snakefile/genomeScore/pval01_annotate_score.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d ${OUTDIR} -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d ${OUTDIR} --latency-wait 60 -pn
~~~

# Genome Score

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
time snakemake -s ${TAGOOS}/snakefile/genomeScore/genomeScore01_makewindow.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d ${OUTDIR} -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d ${OUTDIR} --latency-wait 60 -pn
~~~

_Algo_

- Make single nucleotide peaks for 30000000 windows
- Intersect single nucleotide peaks with regions

Annotate (Region-dependent)

~~~
export GWINDOW_DIR=$PWD/out/data/snp/gwindow
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/genome_score
time snakemake -s ${TAGOOS}/snakefile/genomeScore/genomeScore02_region.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" --latency-wait 60 -d $OUTDIR -pn
~~~

- Annotate region single nucleotide peaks using selected features from models
- Collapse different annotation of single nucleotide
- Collapse single nucleotides with same annotation combinations

~~~
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/annotation/${ANNOT_LABEL}.bed
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export MODEL_PKL=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}/model.pkl
export SCORE2PVAL2NEGLOGPVAL=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/genome_score/random/score2pval2log2pval.tsv
time snakemake -s ${TAGOOS}/snakefile/genomeScore/genomeScore03_annotate.yml -j 64 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -p  -k --rerun-incomplete --latency-wait 60 -n
~~~

ANNOTATION_BED, SCORE_BED AND DBSNP_BED

~~~
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/genome_score/annotation.bed
export SCORE_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/genome_score/score_pval_neglogpval.bg
export DBSNP_BED=$PWD/out/data/snp/dbsnp/${REGION}/dbsnp.bed
~~~

# DB.md ----------------------------

Make window (Region-dependent)

~~~
export DBSIZE=300000000 # larger than largest chromosome
export OUTDIR=${PWD}/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/db
#mkdir -p $OUTDIR
export GENOME_WINDOW_BED=$OUTDIR/genome_splitted.bed
#export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED)
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db01_split_genome.yml -j 256 --keep-going --rerun-incomplete -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

~~~
export GENE_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_RefSeqGenes_geneSymbol.bed
export CHROM="22"
export CHROM="$(seq 1 22)"
export CHROM_WINDOW=2000000 # size of the partitions in the DB
export DBSNP_BED=$PWD/out/data/snp/dbsnp/${REGION}/dbsnp.bed
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db02_intersection.yml -j 192 --keep-going -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

# Enter it into the DB

AnnotationWindow

~~~
#export DB_SERVER="mysql+pymysql://root:mypass@10.1.1.157"

export DB_HOST="localhost"
export DB_HOST="10.1.1.157"
export DB_PORT="3306"

export DB_SERVER="mysql+pymysql://root:mypass@${DB_HOST}:${DB_PORT}"
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db03_mysql.yml -j 192 --keep-going -c "qsub -N '{rule}_{wildcards.chr}' -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d $OUTDIR --latency-wait 60 --resources db=1 -pn
~~~

RSID

~~~
export DB_ID=0
export DB_ID=$(echo {0..19})

export DB_HOST="localhost"
export DB_HOST="10.1.1.157"
export DB_PORT="3306"

export DB_SERVER="mysql+pymysql://root:mypass@${DB_HOST}:${DB_PORT}"
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db04_mysql_rsid.yml -j 192 --keep-going -c "qsub -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d $OUTDIR --latency-wait 60 --resources db=1 -pn
~~~

