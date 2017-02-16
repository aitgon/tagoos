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

library(data.table)

dt = unique(fread(rsidannot_tsv, sep="\t", header=F))
variable2ix = fread(variable_path, header=F)
outdir = dirname(annotation_libsvm)

if (ncol(dt) == 2) { # scores
    colnames(dt) = c("instance", "variable")
    dt$label=-1
    dt$value=1 
} else if (ncol(dt) == 4) { # 4 cols
    colnames(dt) = c('instance', 'value', 'variable', 'label')
    dt = dt[!is.na(as.numeric(as.character(dt$value))),]
} else {
    stop("Neither 2 or 4 cols. File not known")
}

# Variable
colnames(variable2ix) = c("variable")
variable2ix$variable.ix = rownames(variable2ix)

# libsvm
dt=merge(dt, variable2ix, by="variable")
dt$variable.ix_value = paste0(dt$variable.ix, ":", dt$value)
dt = aggregate(variable.ix_value ~ instance + label, data=dt, FUN=function(x) paste(x, collapse=" "))

# add last variable ix to all rows if missing
nrow_variable2ix=nrow(variable2ix)
for (i in 1:nrow(dt)) {
    if (!(nrow_variable2ix %in% dt[1,"variable.ix_value"])){
        dt[i,"variable.ix_value"] = paste0(dt[i,"variable.ix_value"], " ", nrow_variable2ix, ":0")
    }
}

# remove negative that also have postive
dt <- dt[order(dt$label, decreasing=TRUE),]
dt = dt[!duplicated(dt[, c("instance")]),]

# variable index
instance = dt$instance
dt = dt[, c(-1)]

#write.table(variable2ix$variable, file=file.path(outdir, "variable.txt"), col.names=F, row.names=F, quote=F, sep="\t")
write.table(instance, file=file.path(outdir, "instance.txt"), col.names=F, row.names=F, quote=F, sep="\t")
write.table(dt, file=annotation_libsvm, col.names=F, row.names=F, quote=F)

