# Other phenotypes

We have shown the detailed parameters for the GRASP variants. A few other phenotypes are working well with the following parameters.

## Height

~~~
export VARIANT_POSITION=intronic
export TAG_POS_RSID=$HOME/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg10000000
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export LD=0.8
~~~



## Blood pressure

~~~
export VARIANT_POSITION=intronic
export TAG_POS_RSID=$HOME/data/2015_svmgwas/data/variant/literature_association/traits/bloodPressureMerged.rsid
export POS_LABEL=bloodPressureMerged
export NEG_LABEL=1kg10000000
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export LD=0.8
~~~

Create model using a subset of available chromosomes

~~~
export CHROM="3 4 6 8 9 11 12 15 16 17 19 22"
# Go on with model.yml
~~~

## Serum Urate

On the other hand, these phenotypes are not working well but can be kept as negative control

~~~
export VARIANT_POSITION=intronic
export TAG_POS_RSID=$HOME/data/2015_svmgwas/data/variant/literature_association/traits/serumUrateNatGen2013.rsid
export POS_LABEL=serumUrateNatGen2013
export NEG_LABEL=1kg10000000
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export LD=0.8
~~~

## Body-mass-index

~~~
export TAG_POS_RSID=$HOME/MEGA/2015_svmgwas/data/variant/literature_association/traits/bmiNatGen2013.rsid
export POS_LABEL=bmiNatGen2013
export NEG_LABEL=1kg10000000
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export LD=0.8
~~~

## Transmission distortion

~~~
export TAG_POS_RSID=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/transmissionDistortion.rsid
export POS_LABEL=transmissionDistortion
export NEG_LABEL=1kg10000000
export ANNOT_LABEL=mergedannot
export INDEX_LABEL=index3
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
export LD=0.8
~~~

