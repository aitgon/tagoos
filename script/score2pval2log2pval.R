#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)!=2) {
  stop("Four arguments are required", call.=FALSE)
} else if (length(args)==2) {
score_tsv=args[1]
score2pval2log10pval_tsv=args[2]
}

library(data.table);
dt=fread(score_tsv,sep="\t");
score_list=unique(dt$V2);
df=data.frame(score=unique(dt$V2), pval=sapply(unique(dt$V2), function(x) {{sum(dt$V2>x)/nrow(dt)}}));
df = df[df$pval!=0,];
df$neglogpval=-log10(df$pval);
write.table(df, file=score2pval2log10pval_tsv, sep="\t", row.names=F, col.names=F);

