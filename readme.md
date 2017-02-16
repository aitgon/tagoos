/cobelix/gonzalez/Software/miniconda3/envs/svmgwasappli3/bin/python /cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos/script/cv_proba.py 15 /cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos/out/heightMergedNature2010NatGen2014/1kg100000_annotationcorr_index3/annotation.libsvm /cobelix/gonzalez/data/2015_svmgwas/data/annotation_ngs_based/annotationcorr/variable.txt /cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos/out/heightMergedNature2010NatGen2014/1kg100000_annotationcorr_index3/rsid2chrom.tsv /cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos/out/heightMergedNature2010NatGen2014/1kg100000_annotationcorr_index3/cv_proba_path.pkl

paste /cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos/out/heightMergedNature2010NatGen2014/1kg100000_annotationcorr_index3/rsid2chrom.tsv /cobelix/gonzalez/data/2015_svmgwas/repositories/tagoos/out/heightMergedNature2010NatGen2014/1kg100000_annotationcorr_index3/annotation.libsvm >t

/cobelix/gonzalez/data/2015_svmgwas/data/hcomp/build_index -sr="chr" -r="chr" -fs="\t" -f=2 h > h.idx
/cobelix/gonzalez/data/2015_svmgwas/data/hcomp/get_record t.idx t chr8 |cut -f3 >test.libsvm

export LC=ALL=C; time grep -w chr8 t |cut -f3 >test.libsvm
export LC=ALL=C; grep -w -v chr8 t |cut -f3 >train.libsvm

# Commands

Must be run in root folder

- doc/all.md
- doc/...

Results go to "out"

closestBed -a score.bed -b /cobelix/gonzalez/data/2015_svmgwas/data/var/knownGene_hg19.bed  |cut -f4,8 >rsid2gene.tsv

dt=fread("rsid2gene.tsv" , header=F)
dt2=fread("score.tsv")
m=merge(dt2, dt, by.x="V1", by.y="V1")
m = m[order(-rank(V2.x), V1, V2.y)]
options(scipen=999)
write.table(m, "rsid2score2gene.tsv", row.names=F, col.names=F, quote=F)


time /cobelix/gonzalez/data/2015_svmgwas/data/hcomp/build_index -sr="" -r="" -fs="\t" -f=3 index2annot_r2_label.tsv >index2annot_r2_label.tsv.f3.idx

time /cobelix/gonzalez/data/2015_svmgwas/data/hcomp/get_record index2annot_r2_label.tsv.f3.idx index2annot_r2_label.tsv   -f feature/feature_all.txt |awk -F'\t' 'NF==4 {print}' >index2annot_r2_label_feature.tsv
export LC_ALL=C; grep -P "H[34][0-9]+[ACMEacme][0-9]*" t.tsv >t2.tsv

# Install

Create environment conda

~~~
NAME=tagoos
conda create --yes --name $NAME python=3
source activate $NAME
~~~

Install/update packages in conda environment

~~~
conda install --yes --name $NAME --file spec-file.txt
pip install -r requirements.txt
~~~

## Bug

For this error message:

~~~
python: /lib64/libc.so.6: version `GLIBC_2.14' not found
~~~

Fix it like this:

~~~
cd $HOME/Software/miniconda3/envs/tagoos/lib
rm libstdc++.so.6
ln -s $HOME/Software/prefix/lib64/libstdc++.so.6
cd $OLDPWD
~~~

