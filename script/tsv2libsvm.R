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

#dt = get(load(index2annot_r2_tsv))
Sys.time()
dt = fread(index2annot_r2_tsv, sep="\t");
names(dt) = c('instance', 'value', 'variable', 'label')
dt = dt[!is.na(as.numeric(as.character(dt$value))),]
Sys.time()
dt$value = as.numeric(as.character(dt$value))
Sys.time()

Sys.time()
dt$value=round(dt$value, 2)
dt$variable.ix = as.numeric(as.factor(dt$variable))
dt$instance.ix = as.numeric(as.factor(dt$instance))
variable = unique(dt[order(rank(variable, variable)), 'variable', with=F])
#variable = variable[order(variable$variable.ix),]
instance = unique(dt[order(rank(instance, instance)), 'instance', with=F])
#instance = instance[order(instance$instance.ix),]
dt$instance_label = paste0(dt$instance.ix, ":", dt$label)
dt$variable.ix_value = paste0(dt$variable.ix, ":", dt$value)
dt = dt[,c(-1, -2, -3, -4, -5, -6), with=F] # remove instance and variable columns
dt = aggregate(variable.ix_value ~ instance_label, data=dt, FUN=function(x) paste(x, collapse=" "))

Sys.time()
dt$label = str_split_fixed(dt$instance_label, ":", 2)[,2]
dt = dt[,c(3,2)]

write.table(variable, file=file.path(outdir, "variable.txt"), col.names=F, row.names=F, quote=F, sep="\t")
write.table(instance, file=file.path(outdir, "instance.txt"), col.names=F, row.names=F, quote=F, sep="\t")
write.table(dt, file=file.path(outdir, "annotation.libsvm"), col.names=F, row.names=F, quote=F)

