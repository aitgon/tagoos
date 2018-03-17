import sys,math;
chrom = int(sys.argv[1])

chrom_sizes = {1:249250621, 2:243199373, 3:198022430, 4:191154276, 5:180915260, 6:171115067, 7:159138663, 8:146364022, 9:141213431, 10:135534747, 11:135006516, 12:133851895, 13:115169878, 14:107349540, 15:102531392, 16:90354753, 17:81195210, 18:78077248, 20:63025520, 19:59128983, 22:51304566, 21:48129895}
partition_cmd='ALTER TABLE AnnotationWindow PARTITION BY RANGE columns(start_hg19_chromosome_window, start_hg38_chromosome_window)(';
for i in range(1, int(math.floor(chrom_sizes[chrom]/2000000))):
    partition_cmd = partition_cmd + "PARTITION p{} VALUES LESS THAN ({},{}), ".format(i,i,i)

partition_cmd = partition_cmd + "PARTITION pmax VALUES LESS THAN (maxvalue,maxvalue))"
sys.stdout.write(partition_cmd)


