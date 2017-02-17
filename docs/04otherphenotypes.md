# Other phenotypes

We have shown the detailed parameters for the GRASP variants. A few other phenotypes are working well with the following parameters.

## Height

~~~
export TAG_RSID_POS=/cobelix/gonzalez/data/2015_svmgwas/data/variant/literature_association/traits/heightMergedNature2010NatGen2014.rsid
export POS_LABEL=heightMergedNature2010NatGen2014
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotationcorr
export INDEX_LABEL=index3
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
~~~

## Blood pressure

~~~
export TAG_RSID_POS=$HOME/data/2015_svmgwas/data/variant/literature_association/traits/bloodPressureMerged.rsid
export POS_LABEL=bloodPressureMerged
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotationcorr
export INDEX_LABEL=index3
export ANNOT_1COL_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/${ANNOT_LABEL}/${ANNOT_LABEL}_1col.bed
~~~

On the other hand, these phenotypes are not working well but can be kept as negative control

## Serum Urate

~~~
export POS_LABEL=serumUrateNatGen2013
export NEG_LABEL=1kg10000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
~~~

## Body-mass-index

~~~
export TAG_RSID_POS=$HOME/MEGA/2015_svmgwas/data/variant/literature_association/traits/bmiNatGen2013.rsid
export POS_LABEL=bmiNatGen2013
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
~~~

## Transmission distortion

~~~
export TAG_RSID_POS=${HOME}/data/2015_svmgwas/data/variant/GRASP/phenos108/transmissionDistortion.rsid
export POS_LABEL=transmissionDistortion
export NEG_LABEL=1kg100000
export ANNOT_LABEL=annotation
export INDEX_LABEL=index3
~~~

