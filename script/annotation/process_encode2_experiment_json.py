import os, pandas, json
import sys
from json.decoder import JSONDecodeError

def main(argv):
    json_file_dir = sys.argv[1] # json_file_dir = "json_tmp"
    processed_experiment_tsv = sys.argv[2]
    #
    json_files=os.listdir(json_file_dir)
    out_list=[]
    for jf in json_files:
        #print(os.path.join(json_file_dir, jf))
        try:
            with open(os.path.join(json_file_dir, jf)) as data_file: json_data=json.load(data_file)
            a=json_data['@id'].split("%2F")[2]
            for file_dict in json_data['@graph']:
                f = file_dict['href']
                if not file_dict['file_type'] in ["fastq", "bam", "bigWig", "bigBed narrowPeak", "tar", "bigBed broadPeak"]:
                    if not file_dict['status'] in ['archived']:
                        if 'assembly' in file_dict.keys():
                            fid=f.split("/files/")[1].split("/@@download/")[0]
                            file_list = [a, f, fid, file_dict['file_type'], file_dict['output_type'], file_dict['status'], file_dict['assembly']]
                            #print(file_list)
                            out_list.append(file_list)
        except JSONDecodeError:
            print("Oops!  JSONDecodeError...")

    file_df = pandas.DataFrame(out_list)
    file_df.columns = ['Accession', 'Files', 'file_id', 'file_type', 'output_type', 'status', 'assembly']
    file_df['assembly'] = pandas.Categorical(file_df['assembly'], ["hg19", "GRCh38"]) # set order
    file_df['file_type'] = pandas.Categorical(file_df['file_type'], ["bed narrowPeak", "bed broadPeak"]) # set order
    file_df['output_type'] = pandas.Categorical(file_df['output_type'], ["optimal idr thresholded peaks", "replicated peaks", "hotspots", "peaks"]) # set order
    file_df = file_df.sort_values(by=['output_type', 'file_type', 'assembly', 'Accession'])
    file_df.drop_duplicates(subset="Accession", keep="first", inplace=True)
    file_df.to_csv(processed_experiment_tsv, sep="\t", index=False)

if __name__ == "__main__":
    main(sys.argv[1:])

