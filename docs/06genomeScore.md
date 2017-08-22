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
export TAGOOS_APPLI=${HOME}/data/2015_svmgwas/repositories/tagoos-appli
~~~

Make window (Region-independent)

~~~
export GWINDOW_LENGTH=30000000
export OUTDIR=$HOME/data/2015_svmgwas/repositories/tagoos-appli/170712/out/data_snp/gwindow_${GWINDOW_LENGTH}
export GENOME_WINDOW_BED=${OUTDIR}_makewindow/genome_splitted.bed
if [ ! -f $GENOME_WINDOW_BED ]; 
then mkdir -p ${OUTDIR}_makewindow && bedtools makewindows -g ~/MEGA/2015_svmgwas/analysis/170412_genome_regions/hg19.chrom.sizes -w $GWINDOW_LENGTH |uniq  |awk '{print $1"\t"$2"\t"$3"\t"$1":"$2+1"-"$3}' |sort -k1,1 -k2,2n -k3,3n |grep -P "chr[0-9][0-9]?" > $GENOME_WINDOW_BED
fi
export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED | sort)
#export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED | sort|grep -P "^chr10:" |head -n110)
time snakemake -s ${TAGOOS}/snakefile/genomeScore/genomeScore01_makewindow.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d ${OUTDIR}_makewindow -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}_makewindow/stderr.log -o ${OUTDIR}_makewindow/stdout.log" -d ${OUTDIR}_makewindow --latency-wait 60 -pn
~~~

Annotate (Region-dependent)

~~~
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_data/annotation/${ANNOT_LABEL}.bed
export GWINDOW_1NT_DIR=$HOME/data/2015_svmgwas/repositories/tagoos-appli/170712/out/data_snp/gwindow_${GWINDOW_LENGTH}
export OUTDIR=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/score_1nt_${GWINDOW_LENGTH}
time snakemake -s ${TAGOOS}/snakefile/genomeScore/genomeScore02_region.yml -j 64 --keep-going --rerun-incomplete -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" --latency-wait 60 -d $OUTDIR -pn
#
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
export MODEL_PKL=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}/model.pkl
time snakemake -s ${TAGOOS}/snakefile/genomeScore/genomeScore03_annotate.yml -j 64 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -p  -k --rerun-incomplete --latency-wait 60 -n
~~~

ANNOTATION_BED, SCORE_BED AND DBSNP_BED

~~~
export ANNOTATION_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/score_1nt_${GWINDOW_LENGTH}/annotation.bed
export SCORE_BED=$PWD/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/score_1nt_${GWINDOW_LENGTH}/percentile.bed
export DBSNP_BED=$PWD/out/data/snp/dbsnp/${REGION}/dbsnp.bed
~~~

# DB.md ----------------------------

Make window (Region-dependent)

~~~
export DBSIZE=250000000
export OUTDIR=${HOME}/data/2015_svmgwas/repositories/tagoos-appli/170712/out/${POS_LABEL}${REGION}/${NEG_LABEL}${REGION}_${ANNOT_LABEL}_${INDEX_LABEL}_analysis/db_${DBSIZE}
mkdir -p $OUTDIR
export GENOME_WINDOW_BED=$OUTDIR/genome_splitted.bed
export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED)
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db01_split_genome.yml -j 256 --keep-going --rerun-incomplete -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

~~~
export GENE_BED=$HOME/MEGA/2015_svmgwas/analysis/170412_genome_regions/ucsc_hg19_RefSeqGenes_geneSymbol.bed
export GENOME_WINDOW_IDS=chr1_1_249250621
export GENOME_WINDOW_IDS=$(cut -f4 $GENOME_WINDOW_BED |sort)
export DBSNP_BED=$PWD/out/data/snp/dbsnp/${REGION}/dbsnp.bed
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db02_intersection.yml -j 192 --keep-going -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d $OUTDIR --latency-wait 60 -pn
~~~

# Enter it into the DB

AnnotationWindow

~~~
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db03_mysql.yml -j 192 --keep-going -c "qsub -N '{rule}_{wildcards.gwindow}' -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d $OUTDIR --latency-wait 60 --resources db=1 -pn
~~~

RSID

~~~
export DB_ID=0
export DB_ID=$(echo {0..19})
export ASSEMBLY=hg19
date; time snakemake -s ${TAGOOS}/snakefile/genomeScore/db04_mysql_rsid.yml -j 192 --keep-going -c "qsub -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d $OUTDIR --latency-wait 60 --resources db=1 -pn
~~~

Drop databases

~~~
cut -f4 $GENOME_WINDOW_BED | sort |while read GW; do DBSUFFIX=$(echo $GW |tr ":" "_"| tr "-" "_"); export DB=intronic_$DBSUFFIX; echo "drop database if exists ${DB};"; done >out/drop.sql
mysql -u root -p'mypass' -h 10.1.1.157 < out/drop.sql
~~~



