CHR=$1
ANNOT_BED=$2
export OUTDIR=$3

GENOME1K_DATA_DIR=$HOME/data/2015_svmgwas/data/variant/1000genomes
SNP_BED=$GENOME1K_DATA_DIR/${CHR}/${CHR}.peak.bed
TMPFILE=$(mktemp /tmp/abc-script.XXXXXX)

mkdir -p $OUTDIR

echo intersectbed
date
time intersectBed -sorted -a ${SNP_BED} -b ${ANNOT_BED} -wb |awk 'BEGIN{OFS="\t"}{print $1,$2,$3,$4,$8}' >$OUTDIR/annotated.bed
echo

#echo annotation 1 col to n col
#date
#time python -c '''
#import os, pandas
#outdir=os.getenv("OUTDIR")
#i=1
#import datetime; print(i,datetime.datetime.now())
#df=pandas.read_csv(os.path.join(outdir, "annotated.bed"), sep="\t", header=None)
#i=2
#import datetime; print(i,datetime.datetime.now())
#df.columns = ("chrom", "chrom_start", "chrom_end", "rsid", "annotation")
#df["r2"]=1
#df2=df.pivot(columns="annotation", values="r2")
#df2.fillna(0, inplace=True)
#df2.insert(0, "chrom", value=df["chrom"])
#df2.insert(1, "chrom_start", value=df["chrom_start"])
#df2.insert(2, "chrom_end", value=df["chrom_end"])
#i=3
#import datetime; print(i,datetime.datetime.now())
#import pdb; pdb.set_trace()
#df2.to_csv(os.path.join(outdir, "annotation_matrix.bed"), sep="\t", index=False, index_label="", header=None, encoding="ascii")
#i=4
#import datetime; print(i,datetime.datetime.now())
#pandas.Series(df2.columns).to_csv(os.path.join(outdir, "header.txt"), index=False)
#'''
#echo

echo annotation 1 col to n col
date
time Rscript -e '''library(data.table); outdir=Sys.getenv(c("OUTDIR")); dt=fread(file.path(outdir, "annotated.bed")); dt = unique(dt); names(dt)=c("chrom", "chrom_start", "chrom_end", "rsid", "annotation"); dt$r2=1; dt2=dcast(dt, chrom + chrom_start + chrom_end + rsid~annotation, value.var="r2"); fwrite(dt2, file.path(outdir, "annotation_matrix.bed"), sep="\t", col.names=FALSE)'''
echo

echo bgzip
date
time bgzip -f $OUTDIR/annotation_matrix.bed
echo

echo tabix
date
time tabix out_chr22_eenhancer_1col.bed/annotation_matrix.bed.gz
echo

echo

