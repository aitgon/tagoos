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

echo annotation 1 col to n col
date
time Rscript -e '''library(data.table); outdir=Sys.getenv(c("OUTDIR")); dt=fread(file.path(outdir, "annotated.bed")); dt = unique(dt); names(dt)=c("chrom", "chrom_start", "chrom_end", "rsid", "annotation"); dt$r2=1; dt3=dcast(dt, rsid~annotation, value.var="r2", fill=0); fwrite(dt3, file.path(outdir, "annotation_matrix_rsid.tsv"), sep="\t", col.names=TRUE)'''
echo

echo build index
date
/gpfs/tgml/apps/build_index -sr="^rs" -r="^rs" -fs="\t" -f=1 $OUTDIR/annotation_matrix_rsid.tsv >$OUTDIR/annotation_matrix_rsid.tsv.idx
echo

echo

