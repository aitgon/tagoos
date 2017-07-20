# NGS annotation data

We have selected these annotation data sources:

- Encode
- Encode2
- [Expressed Enhancers](http://enhancer.binf.ku.dk/presets/)
- GTEx
- ReMap
- Roadmap

We aggregate all data into a single BED file, where the string in the fourth column is created in the following way:

~~~
<databasename>.<experimentid>.<biosample>-<biosamplegroup>.<moleculartarget>
~~~

The field "databasename" is the data source name, eg "encode2".
The field "experimentid" if available is specific to each data source.
The field "biosample" takes a normalized value representing the cell type or tissue of the experiments, eg. "k562", "isletprecursorcell".
The field "biosamplegroup" takes a value from this table representing a tissue or organ for the given cell type or tissue such as "tcell" or brain.
The field "moleculartarget" represent the molecular target of the experiment and takes values such as "h3k27ac", "dnaaseseq" or "gfp-zfp".

General variable

~~~
export THREADS=16
export QUEUE=batch
~~~

## EEnhancer

~~~
export EENHANCER_URL=http://enhancer.binf.ku.dk/presets/
export EENHANCER_DATA_DIR=$PWD/out/data/annotation/eenhancer
time snakemake -s ${TAGOOS}/snakefile/data_annotation/eenhancer.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $EENHANCER_DATA_DIR/stderr.log -o $EENHANCER_DATA_DIR/stdout.log" -d $EENHANCER_DATA_DIR -pn
~~~

## Encode2

- Go to https://www.encodeproject.org/matrix/?type=Experiment
- Select:
    * Organism: Homo sapiens
    * Assay category: DNA binding, DNA accessibility
    * Genome assemby: hg19
    * Available data: bed narrow Peak
- 3366 results
- Click "table-tab-icon"
- Download TSV
- Save to __/cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos-appli/170618/data/encode2_report.tsv__

~~~
export ENCODE2_EXPERIMENT_LIST=$PWD/out/data/annotation/encode2_report.tsv
export ENCODE2_DATA_DIR=$PWD/out/data/annotation/encode2
time snakemake -s ${TAGOOS}/snakefile/data_annotation/encode2.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $ENCODE2_DATA_DIR/stderr.log -o $ENCODE2_DATA_DIR/stdout.log" -d $ENCODE2_DATA_DIR -pn
~~~

## GTEx

~~~
export ANNOTATION_DIC=${TAGOOS}/data/gtex.tsv
export GTEX_DATA_DIR=$PWD/out/data/annotation/gtex
time snakemake -s ${TAGOOS}/snakefile/data_annotation/gtex.yml -p -j 16 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $GTEX_DATA_DIR/stderr.log -o $GTEX_DATA_DIR/stdout.log" -d $GTEX_DATA_DIR -pn
~~~

## ReMap

~~~
export ANNOTATION_DIC=${TAGOOS}/data/remap.tsv
export REMAP_URL=http://tagc.univ-mrs.fr/remap/download/All/filPeaks_all.bed.gz
export REMAP_DATA_DIR=$PWD/out/data/annotation/remap
time snakemake -s ${TAGOOS}/snakefile/data_annotation/remap.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $ROADMAP_DATA_DIR/stderr.log -o $REMAP_DATA_DIR/stdout.log" -d $REMAP_DATA_DIR -pn
~~~

## Roadmap

~~~
export ANNOTATION_DIC=${TAGOOS}/data/roadmap.tsv
export ROADMAP_DATA_DIR=$PWD/out/data/annotation/roadmap
time snakemake -s ${TAGOOS}/snakefile/data_annotation/roadmap.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $ROADMAP_DATA_DIR/stderr.log -o $ROADMAP_DATA_DIR/stdout.log" -d $ROADMAP_DATA_DIR -pn
~~~

## Young H3K27ac

~~~
export ANNOTATION_DIC=${TAGOOS}/data/youngh3k27ac.tsv
export YOUNGH3K27AC_URL=http://www.cell.com/cms/attachment/2021776442/2041649929/mmc8.zip
export YOUNGH3K27AC_DATA_DIR=$PWD/out/data/annotation/youngh3k27ac
time snakemake -s ${TAGOOS}/snakefile/data_annotation/youngh3k27ac.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $YOUNGH3K27AC_DATA_DIR/stderr.log -o $YOUNGH3K27AC_DATA_DIR/stdout.log" -d $YOUNGH3K27AC_DATA_DIR -pn
~~~

## Merged all beds into a single one

~~~
export ANNOT_LABEL=mergedannot
#
export MERGED_DATA_DIR=$PWD/out/data/annotation/${ANNOT_LABEL}
time snakemake -s ${TAGOOS}/snakefile/data_annotation/merge_annotations.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $MERGED_DATA_DIR/stderr.log -o $MERGED_DATA_DIR/stdout.log" -d $MERGED_DATA_DIR -pn
~~~

# Split annotations by chromosoms

~~~
export ANNOT_LABEL=mergedannot
#
export ANNOTATION_BED=$PWD/out/data/annotation/${ANNOT_LABEL}/${ANNOT_LABEL}.bed
export ANNOTATION_DIR=$(dirname ${ANNOTATION_BED})
#
export CHROM="$(seq 1 22) X"
time snakemake -s ${TAGOOS}/snakefile/data_annotation/split_annotation.yml -p -j 32 --keep-going --rerun-incomplete -c "qsub -X -V -q ${QUEUE} -l nodes=1:ppn={threads},walltime=48:00:00 -e $ANNOTATION_DIR/stderr.log -o $ANNOTATION_DIR/stdout.log" -d $ANNOTATION_DIR -pn
~~~


