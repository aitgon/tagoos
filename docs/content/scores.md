# Scores and annotations

## Remote access

Download and install TABIX. Then retrieve scores and annotations remotely in the command line. For instance for the SNP rs227727 (hg19, chr17:54776955-54776955)

~~~
tabix http://pedagogix-tagc.univ-mrs.fr/~gonzalez/tagoos/files/tagoos_intergenic_hg19.bed.gz chr17:54776955-54776955
~~~

Output columns are described here.

## Local access

If you plan to retrieve score often, it is better to download BED.GZ and TBI files and use TABIX locally. The same example with a local file:

~~~
tabix tagoos_intergenic_hg19.bed.gz chr17:54776955-54776955
~~~

