create table IF NOT EXISTS rsidtable (rsid text primary key, posid text not null, gene text not null, distance integer not null, genomic real null, intronic real null, intergenprox real null, intergendistal real null);
.separator " "
.import TSV_PATH rsidtable
