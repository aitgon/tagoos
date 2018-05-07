Region variables

$REGION \in {'intronic', 'intergenic'}$

~~~
export REGION=intronic # default intronic
~~~

~~~
export RELEASE=180328
export PREDICT_DIR=$PWD/out/${REGION}/predict
export OUTDIR=$PWD/out/${REGION}/public
time snakemake -s ${TAGOOS}/snakefile/07public/01public.yml -j 64 -c "qsub -X -V -d $OUTDIR -q ${QUEUE} -l nodes=1:ppn={threads},walltime=12:00:00 -e $OUTDIR/stderr.log -o $OUTDIR/stdout.log" -d $OUTDIR -p  -k --latency-wait 60 -n
~~~

Send to pedagogix

~~~
ssh gonzalez@pedagogix mkdir -p /home/gonzalez/public_html/tagoos/release/${RELEASE}
rsync -avz --progress /cobelix/gonzalez/Data/2015_svmgwas/repositories/tagoos-appli/180328/out/${REGION}/public/release/${RELEASE} gonzalez@pedagogix:/home/gonzalez/public_html/tagoos/release/${RELEASE}
~~~

