#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=3) {
  stop("Four arguments are required", call.=FALSE)
} else if (length(args)==3) {
index2tag2corr_r2_tsv=args[1]
annotation_tsv = args[2]
index2annot_r2_tsv=args[3]
}

library(data.table)
#annotdir=Sys.getenv(c("ANNOTDIR"))
#outdir=Sys.getenv(c("OUTDIR"))

ldlocus=fread(index2tag2corr_r2_tsv, sep="\t")

if (dim(ldlocus)[1] > 0) {
    ldlocus = unique(ldlocus[,c("index", "corr", "index2corr_r2"), with=FALSE])

    annotation=fread(annotation_tsv, sep="\t", header=FALSE)
    names(annotation) = c("rsid", "annotation")

    index2annot_r2 = unique(merge(ldlocus, annotation, all=FALSE, by.x=c('corr'), by.y=c('rsid'), allow.cartesian=TRUE))
    index2annot_r2 = index2annot_r2[, c("index", "index2corr_r2", "annotation"), with=FALSE]
    write.table(index2annot_r2, index2annot_r2_tsv, quote=FALSE, sep="\t", row.names=FALSE, col.names=FALSE)
    #save(index2annot_r2, file=file.path(outdir, "index2annot_r2.Rda"))
} else {
file.create(index2annot_r2_tsv)
}

