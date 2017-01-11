#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=2) {
  stop("Two arguments are required", call.=FALSE)
} else {
index2annot_r2_tsv=args[1]
outdir = args[2]
}

#index2annot_r2_tsv=Sys.getenv(c("INDEX2ANNOT_R2_TSV"))
#outdir=Sys.getenv(c("OUTDIR"))

library(data.table)
library(stringr)

dt = unique(fread(index2annot_r2_tsv, sep="\t"));
names(dt) = c('instance', 'value', 'variable', 'label')

dt = dt[!is.na(as.numeric(as.character(dt$value))),]
#dt$value = as.numeric(as.character(dt$value))

# variable index
dt$value=round(dt$value, 2)
dt$variable.ix = as.numeric(as.factor(dt$variable))
variable2ix=unique(dt[, c("variable", "variable.ix"), with=F])
dt = dt[, c(-3)]
variable2ix <- variable2ix[order(variable2ix$variable.ix, decreasing=F),]

# libsvm
dt$variable.ix_value = paste0(dt$variable.ix, ":", dt$value)
dt = aggregate(variable.ix_value ~ instance + label, data=dt, FUN=function(x) paste(x, collapse=" "))

# remove negative that also have postive
dt <- dt[order(dt$label, decreasing=TRUE),]
dt = dt[!duplicated(dt[, c("instance")]),]

# variable index
#dt$instance.ix = as.numeric(as.factor(dt$instance))
instance = dt$instance
dt = dt[, c(-1)]


# instance index
#instance2ix=dt[, c("instance", "instance.ix")]
#instance2ix <- instance2ix[order(instance2ix$instance.ix, decreasing=F),]
#dt = dt[, c(-1, -2)]

write.table(variable2ix$variable, file=file.path(outdir, "variable.txt"), col.names=F, row.names=F, quote=F, sep="\t")
write.table(instance, file=file.path(outdir, "instance.txt"), col.names=F, row.names=F, quote=F, sep="\t")
write.table(dt, file=file.path(outdir, "annotation.libsvm"), col.names=F, row.names=F, quote=F)

