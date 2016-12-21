Test eur, encode2

~~~
CHR=eur
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/encode2_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate_1kg.sh $CHR $ANNOT_BED $OUTDIR
~~~

Test eur, eenhancer

~~~
CHR=eur
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/eenhancer_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate_1kg.sh $CHR $ANNOT_BED $OUTDIR
# 3 min
~~~

Test chr22, eenhancer

~~~
CHR=chr22
ANNOT_BED=$HOME/data/2015_svmgwas/data/annotation_ngs_based/eenhancer_1col.bed
OUTDIR=out_${CHR}_$(basename ${ANNOT_BED})
time bash annotate_1kg.sh $CHR $ANNOT_BED $OUTDIR
# 16 s
~~~

# Archive

~~~
import pandas
df=pandas.read_csv("annotated.bed", sep="\t", header=None)
df.columns = ("chrom", "chrom_start", "chrom_end", "rsid", "annotation")
df['r2']=1
df2=df.pivot(columns='annotation', values='r2')
df2.fillna(0, inplace=True)
df2.insert(0, 'chrom', value=df['chrom'])
df2.insert(1, 'chrom_start', value=df['chrom_start'])
df2.insert(2, 'chrom_end', value=df['chrom_end'])
df2.to_csv("annotation_matrix.bed", sep="\t", index=False, index_label="")
pandas.Series(df2.columns).to_csv("header.txt", index=False)
~~~

~~~
library(data.table)
dt=fread("annotated.bed")
dt=unique(dt)
names(dt)=c("chrom", "chrom_start", "chrom_end", "rsid", "annotation")
dt$r2=1
dt2=dcast(dt, chrom + chrom_start + chrom_end + rsid~annotation, value.var="r2")
fwrite(dt2, "annotation_matrix.bed", sep="\t", col.names=FALSE)
~~~


