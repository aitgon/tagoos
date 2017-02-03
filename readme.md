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

