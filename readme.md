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

