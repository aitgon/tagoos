library(data.table)
annotdir=Sys.getenv(c("ANNOTDIR"))
outdir=Sys.getenv(c("OUTDIR"))

ldlocus=fread(file.path(outdir, "index2tag2corr_ld.tsv"), sep="\t")
ldlocus = unique(ldlocus[,c("index", "corr", "index2corr_r2")])

annotation=fread(file.path(annotdir, "annotated.tsv"), sep="\t", header=FALSE)
names(annotation) = c("rsid", "annotation")

index2annot_r2 = unique(merge(ldlocus, annotation, all=FALSE, by.x=c('corr'), by.y=c('rsid'), allow.cartesian=TRUE))
index2annot_r2 = index2annot_r2[, c("index", "index2corr_r2", "annotation")]
write.table(index2annot_r2, file.path(outdir, "index2annot_r2.tsv"), quote=FALSE, sep="\t", row.names=FALSE)
save(index2annot_r2, file=file.path(outdir, "index2annot_r2.Rda"))

