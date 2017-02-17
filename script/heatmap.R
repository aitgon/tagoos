#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

library(data.table)
library(gplots)

# test if there is at least one argument: if not, return an error
if (length(args)!=4) {
  stop("Four arguments are required", call.=FALSE)
} else if (length(args)==4) {
index2annot_r2_label_tsv=args[1]
all_features_txt=args[2]
heatmap_detailed_pdf=args[3]
heatmap_classes_pdf=args[4]
}

dt=fread(index2annot_r2_label_tsv)
colnames(dt)=c("rsid", "r2", "feature", "label")

# selected feature
best_feature=fread(all_features_txt)
dt2=dt[dt$feature %in% best_feature$feature,]

# remove duplicated with highest R2 and class
dt2 <- dt2[order(-dt2$r2, -dt2$label ), ]
dt2= dt2[ !duplicated(dt2[, c("rsid", "feature", "label"), with=F]), ]

dc=dcast(dt2, rsid+label ~feature, value.var="r2", fill=0)

browser()
# keep max 10000 in neg
keep.neg=10000
keep.pos=10000
#if ((length(which(dc$label==-1)) > keep.neg) | (length(which(dc$label==1)) > keep.pos)) {
keep.idx = sample(which(dc$label==1), keep.pos)
keep.idx = c(keep.idx, sample(which(dc$label==-1), keep.neg))
dc = dc[keep.idx,]
}

m=as.matrix(dc[,3:ncol(dc)])
m=t(m)

colsidecolors=1:ncol(m)
colsidecolors[dc$label[1:ncol(m)]==1]="black"
colsidecolors[dc$label[1:ncol(m)]==-1]="white"

legend=c("EZH2", "H2AC1", "H2AFZ", "H3F3A", "H3K4me1", "H3K4me2", "H3K9ac", "H3K9me3", "H3K27ac", "H3K27me3", "H3K36me3", "H3K79me2", "H4K20me1", "HDAC6", "enhancer_tss_associations", "POLR2A")
require(RColorBrewer)
colorset=unique(c(brewer.pal(11, "PRGn"), brewer.pal(11, "RdBu")))
col=colorset[1:length(legend)]

rowsidecolors=1:nrow(m)
rowsidecolors[1:nrow(m)]="white"
for (i in 1:length(legend)) {
rowsidecolors[grep(legend[i], colnames(dc)[3:length(colnames(dc))], ignore.case=TRUE)]=col[i]
}

pdf(heatmap_detailed_pdf, paper="a4", width=20, height=20)
heatmap.2(m, scale = "none", col=colorRampPalette(c("white", "red"))(256), ColSideColors=colsidecolors, RowSideColors=rowsidecolors, dendrogram='none', trace='none', density.info = "none", key=FALSE, lwid=c(0.1,4), lhei=c(0.1,4), margins=c(5,20), cexRow=0.5)
dev.off()

pdf(heatmap_classes_pdf, paper="a4", width=20, height=20)
heatmap.2(m, scale = "none", col=colorRampPalette(c("white", "red"))(256), ColSideColors=colsidecolors, RowSideColors=rowsidecolors, dendrogram='none', trace='none', density.info = "none", key=FALSE, lwid=c(0.1,4), lhei=c(0.1,4), margins=c(5,20), labRow=F, labCol=F)
par(lend = 1)           # square line ends for the color legend
legend("topright",      # location of the legend on the heatmap plot
    legend = legend, # category labels
    col = col,  # color key
    lty= 1,             # line style
    lwd = 10            # line width
)
dev.off()


