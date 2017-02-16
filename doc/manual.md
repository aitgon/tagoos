# Tagoos Workflow

For the tagoos workflow, there are preprocessing steps with these snakefiles

- split annotation: __split_annotation.yml__
- annotate 1000 genome data: __preannotate.yml__ with 1000 genome parameters
- annotate dbsnp: __preannotate.yml__ with dbsnp parameters
- LD and index calculation of 1000 genome data: __genome1k.yml__

Then we can create a model and score the dbsnp with these snakefiles

- Create a specific model: __Snakemake.yml__
- Score some data: __Snakemake_score.yml__
- Score the dbsnp database with a specific model: __score_dbsnp.yml__

