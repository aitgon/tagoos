% Tagoos Documentation
% Aitor Gonzalez

# Overview

This is an overview of the tagoos workflow. There are two large parts. 

1. Process 1000 genome and dbsnp variants with NGS data:
2. Create a model and score the dbsnp variants

In order to create a model, these parameters are needed:

- A positive RSID list
- (Optional) A list of negative random SNPs from the 1000 genome database
- (Optional) An annotation file in bed format: annotationcorr
- (Optional) A precomputed index file: index, index2 or index3

In order to carry out there are two large parts

1. The preprocessing step where 1000 genome and dbsnp variants are processed and annotated with NGS data
2. The modeling and scoring of the dbsnp variants.

The first part of the workflow is carried out in the following manner

- split annotation: __split_annotation.yml__ :ref:`genindex`
- annotate 1000 genome data: __preannotate.yml__ with 1000 genome parameters
- annotate dbsnp: __preannotate.yml__ with dbsnp parameters
- LD and index calculation of 1000 genome data: __genome1k.yml__

The second part of the workflow is carried out in the following manner

- Create a specific model: __Snakemake.yml__
- Score the dbsnp database with a specific model: __score_dbsnp.yml__

