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

## Encode2

~~~
export ENCODE2_URL="https://www.encodeproject.org/report.tsv?type=Experiment&replicates.library.biosample.donor.organism.scientific_name=Homo+sapiens&assembly=hg19&assay_title=ChIP-seq&assay_title=DNase-seq&assay_title=FAIRE-seq&assay_slims=DNA+accessibility&assay_slims=DNA+binding&files.file_type=bed+narrowPeak&field=%40id&field=accession&field=assay_term_name&field=assay_title&field=target.label&field=target.gene_name&field=biosample_summary&field=biosample_term_name&field=description&field=lab.title&field=award.project&field=status&field=replicates.biological_replicate_number&field=replicates.technical_replicate_number&field=replicates.antibody.accession&field=replicates.library.biosample.organism.scientific_name&field=replicates.library.biosample.life_stage&field=replicates.library.biosample.age&field=replicates.library.biosample.age_units&field=replicates.library.biosample.treatments.treatment_term_name&field=replicates.library.biosample.treatments.treatment_term_id&field=replicates.library.biosample.treatments.concentration&field=replicates.library.biosample.treatments.concentration_units&field=replicates.library.biosample.treatments.duration&field=replicates.library.biosample.treatments.duration_units&field=replicates.library.biosample.synchronization&field=replicates.library.biosample.post_synchronization_time&field=replicates.library.biosample.post_synchronization_time_units&field=replicates.%40id&field=files"
export ENCODE2_EXPERIMENT_LIST=${TAGOOS}/data/encode2_data2.tsv
export ANNOTATION_DATA=${TAGOOS}/data/annotation_data2.tsv
export ENCODE2_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/encode2
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/encode2.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ENCODE2_DATA_DIR/stderr.log -o $ENCODE2_DATA_DIR/stdout.log" -d $ENCODE2_DATA_DIR -pn
~~~

## GTEx

~~~
export ANNOTATION_DATA=${TAGOOS}/data/annotation_data2.tsv
export GTEX_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/gtex
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/gtex.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $GTEX_DATA_DIR/stderr.log -o $GTEX_DATA_DIR/stdout.log" -d $GTEX_DATA_DIR -pn
~~~

## ReMap

~~~
export ANNOTATION_DATA=${TAGOOS}/data/annotation_data2.tsv
export REMAP_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/remap
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/remap.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ROADMAP_DATA_DIR/stderr.log -o $REMAP_DATA_DIR/stdout.log" -d $REMAP_DATA_DIR -pn
~~~

## Roadmap

~~~
export ANNOTATION_DATA=${TAGOOS}/data/annotation_data2.tsv
export ROADMAP_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/roadmap
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/roadmap.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ROADMAP_DATA_DIR/stderr.log -o $ROADMAP_DATA_DIR/stdout.log" -d $ROADMAP_DATA_DIR -pn
~~~

## Young H3K27ac

~~~
export ANNOTATION_DATA=${TAGOOS}/data/annotation_data2.tsv
export YOUNGH3K27AC_DATA_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based/youngh3k27ac
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/youngh3k27ac.yml -p -j 16 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $YOUNGH3K27AC_DATA_DIR/stderr.log -o $YOUNGH3K27AC_DATA_DIR/stdout.log" -d $YOUNGH3K27AC_DATA_DIR -pn
~~~

## Merged all beds into a single one

~~~
export ANNOTATION_DIR=$HOME/data/2015_svmgwas/data/annotation_ngs_based
export THREADS=8
time snakemake -s ${TAGOOS}/snakefile/annotation/merge_annotations.yml -p -j 32 -c "qsub -X -V -q tagc -l nodes=1:ppn={threads} -e $ANNOTATION_DIR/stderr.log -o $ANNOTATION_DIR/stdout.log" -d $ANNOTATION_DIR -pn
~~~

# Split annotations by chromosoms

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


