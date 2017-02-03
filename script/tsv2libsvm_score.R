#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=3) {
  stop("Two arguments are required", call.=FALSE)
} else {
rsidannot_tsv=args[1]
variable_path=args[2]
annotation_libsvm = args[3]
}

outdir = dirname(annotation_libsvm)

library(data.table)
rsidannot = fread(rsidannot_tsv, sep="\t", header=F)
colnames(rsidannot) = c("instance", "variable")
rsidannot$label=-1
#
variable = fread(variable_path, header=F)
colnames(variable) = c("variable")
variable$variable.ix = rownames(variable)
variable$variable.ix_value = paste0(variable$variable.ix, ":1")
#
dt=merge(rsidannot, variable, by="variable")
dt = aggregate(variable.ix_value ~ instance + label, data=dt, FUN=function(x) paste(x, collapse=" "))

# if not last var in any row, append it with 0
lastvarix=dim(variable)[1]
#if (length(grep(lastvarix, dt$variable.ix_value)) == 0) {
if (!(lastvarix %in% dt[1,]$variable.ix_value)) {
    dt[1,]$variable.ix_value = paste0(dt[1,]$variable.ix_value, " ", lastvarix, ":0")
}

instance = dt$instance
dt = dt[, c(-1)]
write.table(dt, file=annotation_libsvm, col.names=F, row.names=F, quote=F)
write.table(instance, file=file.path(outdir, "instance.txt"), col.names=F, row.names=F, quote=F, sep="\t")





