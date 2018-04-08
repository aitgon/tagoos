# Model learning

In this example we create a model for

- Associated GRASP variants ($p-val lower than 10^8$)
- 100000 random variants for the 1000 genome DB
- The __annotationcorr__ variants
- The __index__ variants


Region variables

$REGION \in {'intronic', 'intergenic'}$

~~~
export REGION=intronic # default intronic intergenic
export CHROM="$(seq 22)"
#export CHROM="22"
~~~

~~~
export THREADS=16 # default 8
export QUEUE=tagc # default batch
export PYTHONBIN=$(which python)
~~~

~~~
export LD_R2=08
export LD_DIR=${PWD}/out/data/snp/1000genomes/${REGION}/ld${LD_R2}/chrom
export INDEX_DIR=${PWD}/out/data/snp/1000genomes/${REGION}/index3/chrom
export FIN_ID2VARIABLE_TSV=${PWD}/out/data/annotation/mergedannot/id2variable.tsv
export ANNOTATION_ID_MAX=$(sort -k1,1nr ${FIN_ID2VARIABLE_TSV} |head -n1 |cut -f 1)
export GENOME1K_PEAK_BED_DIR=${PWD}/out/data/snp/1000genomes/${REGION}/peak_bed
export POS_RSID=${PWD}/out/data/snp/grasp/${REGION}/grasp108.int.rsid
export VARIABLE_TXT=$PWD/out/data/annotation/${ANNOT_LABEL}/variable.txt
#
export OUTDIR=${PWD}/out/intronic/model/chrom
mkdir -p ${OUTDIR}
time snakemake -s ${TAGOOS}/snakefile/05model/01training_matrix.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e ${OUTDIR}/stderr.log -o ${OUTDIR}/stdout.log" -d ${OUTDIR} --latency-wait 60 -pn
~~~


