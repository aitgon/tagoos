#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=4) {
  stop("Four arguments are required", call.=FALSE)
} else if (length(args)==4) {
ld=args[1]
index_rsid_path=args[2]
tag_rsid_path=args[3]
index2tag2corr_r2_tsv=args[4]
}

library(data.table)
dt=fread(ld)
dt=dt[,c("SNP_A", "SNP_B", "R2"),with=FALSE]
names(dt)=c("snpa", "snpb", "r2")
setkey(dt, snpa)

# index
# indexindex - indexcorr
#index_rsid_path="/cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/chr22/chr22_index.prune.in"
index=fread(index_rsid_path, col.names=c("snpa"))
setkey(index, snpa)
indexld = unique(dt[dt$snpa %in% index$snpa, ])
#setkey(indexld, snpa)

# tag
# tagindex - tagcorr
#tag_rsid_path="/cobelix/gonzalez/data/2015_svmgwas/data/variant/GRASP/GRASP108.rsid"
tag=fread(tag_rsid_path, col.names=c("snpa"))
setkey(tag, snpa)
tagld = unique(dt[dt$snpa %in% tag$snpa, ])

# index2tag2tagcorr_r2
# merge: indexcorr=tagtag
# indexindex2tagtag_r2 - tag.tag2tag.corr_r2
setkey(indexld, snpb)
setkey(tagld, snpa)
index2tag2tagcorr_r2 = unique(merge(indexld, tagld, all=FALSE, by.x=c('snpb'), by.y=c('snpa'), allow.cartesian=TRUE))
names(index2tag2tagcorr_r2) = c("index", "tag", "index2tag_r2", "tagcorr", "tag2tagcorr_r2")

# index2tag2commoncorr
setkey(index2tag2tagcorr_r2, tagcorr)
#m = merge(index2tag2tagcorr_r2, indexld, all=FALSE, by.x=c('index', 'tagcorr'), by.y=c('snpa', 'snpb'), allow.cartesian=TRUE)
locusld = merge(index2tag2tagcorr_r2, indexld, all=FALSE, by.x=c('index', 'tagcorr'), by.y=c('snpa', 'snpb'), allow.cartesian=TRUE)
names(locusld)=c("index", "corr", "tag", "index2tag_r2", "tag2corr_r2", "index2corr_r2")
locusld = locusld[,c("index", "tag", "corr", "index2tag_r2", "index2corr_r2", "tag2corr_r2"), with=FALSE]
write.table(locusld, index2tag2corr_r2_tsv, quote=FALSE, sep="\t", row.names=FALSE)

