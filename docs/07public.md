Region variables

$REGION \in {'intronic', 'intergenic'}$

~~~
export REGION=intergenic # intronic or intergenic
~~~

~~~
export QUEUE=tagc
export THREADS=16
~~~

# Tabix output

~~~
export RELEASE=180328
export PREDICT_DIR=$PWD/out/${REGION}/predict
export OUTDIR=$PWD/out/${REGION}/public
time snakemake -s ${TAGOOS}/snakefile/07public/01public.yml -j 64 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -p  -k --latency-wait 60 -n
~~~

# neg log10 pval BigWig and annotation BigBed for UCSC

~~~
export ASSEMBLY=hg19
export CHROM_SIZES_URL=hgdownload.cse.ucsc.edu/goldenPath/${ASSEMBLY}/bigZips/${ASSEMBLY}.chrom.sizes
export CHROM_SIZES_URL_DIR=$(dirname $CHROM_SIZES_URL)
export CHROM_SIZES_DIR=${HOME}/Data/public/${CHROM_SIZES_URL_DIR}
mkdir -p ${CHROM_SIZES_DIR}
wget -N http://${CHROM_SIZES_URL} -P ${CHROM_SIZES_DIR}
export CHROM_SIZES_HG19=${HOME}/MEGA/2015_svmgwas/analysis/170412_genome_regions/raw_hg19.chrom.sizes
~~~

~~~
export ASSEMBLY=hg38
export CHROM_SIZES_URL=hgdownload.cse.ucsc.edu/goldenPath/${ASSEMBLY}/bigZips/${ASSEMBLY}.chrom.sizes
export CHROM_SIZES_URL_DIR=$(dirname $CHROM_SIZES_URL)
export CHROM_SIZES_DIR=${HOME}/Data/public/${CHROM_SIZES_URL_DIR}
mkdir -p ${CHROM_SIZES_DIR}
wget -N http://${CHROM_SIZES_URL} -P ${CHROM_SIZES_DIR}
export CHROM_SIZES_HG38=${HOME}/MEGA/2015_svmgwas/analysis/170412_genome_regions/raw_hg19.chrom.sizes
~~~

~~~
export PREDICT_DIR=$PWD/out/${REGION}/predict
export UCSC_DIR=$PWD/out/${REGION}/ucsc
time snakemake -s ${TAGOOS}/snakefile/07public/02ucsc.yml -j 64 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -p  -k --latency-wait 60 -n
~~~

# Send to pedagogix

~~~
ssh gonzalez@pedagogix mkdir -p /home/gonzalez/public_html/tagoos/release/${RELEASE}
rsync -n -avz --progress /cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/${REGION}/public/release/${RELEASE}/ gonzalez@pedagogix:/home/gonzalez/public_html/tagoos/release/${RELEASE}/
~~~

