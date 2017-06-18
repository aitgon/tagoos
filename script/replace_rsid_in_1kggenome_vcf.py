import sys,csv

if len(sys.argv)==4:
    vcf_path=sys.argv[1]
    posid2rsid_path=sys.argv[2]
    vcfout_path=sys.argv[3]
elif len(sys.argv)==3:
    #vcf_path=sys.argv[2] STDIN
    posid2rsid_path=sys.argv[1]
    vcfout_path=sys.argv[2]

posid2rsid_d = dict()
with open(posid2rsid_path) as posid2rsid_fin:
     for line in posid2rsid_fin:
        (key, val) = line.split()
        posid2rsid_d[key] = val


#fin_vcf = "/cobelix/gonzalez/data/2015_svmgwas/data/variant/1000genomes/raw/chr1.vcf"

# parse command line
#import pdb; pdb.set_trace()
try:
    vcf_reader = csv.reader(open(vcf_path, 'r'), delimiter="\t")
except:
    vcf_reader = csv.reader(sys.stdin, delimiter="\t")

unique_posid_d = dict()

with open(vcfout_path, 'w') as vcfout_fout:
    for line in vcf_reader:
        if line[0].startswith("#"):
            vcfout_fout.write("\t".join(line) + "\n")
        else:
            posid = "chr%s:%d"%(str(line[0]), int(line[1]))
            if posid in posid2rsid_d and not posid in unique_posid_d:
                unique_posid_d[posid] = None # keep unique list of posids
                line[2] = posid2rsid_d[posid]
                vcfout_fout.write("\t".join(line) + "\n")


