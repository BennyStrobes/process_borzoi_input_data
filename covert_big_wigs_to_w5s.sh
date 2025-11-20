#!/bin/bash
#SBATCH -t 0-7:30                         # Runtime in D-HH:MM format
#SBATCH -p bch-compute                        # Partition to run in
#SBATCH --mem=10GB 




gtex_bigwig_summary_file="${1}"
w5_dir="${2}"
borzoi_code_dir="${3}"
w5_qc_dir="${4}"
gtex_targets_file="${5}"

source ~/.bashrc
conda activate borzoi

tail -n +2 $gtex_bigwig_summary_file | while read -r col1 sample_id bw_file rest; do

	echo $sample_id"  "${bw_file}
	w5_file=${w5_dir}${sample_id}".w5"

	python bw_h5_custom.py -z $bw_file $w5_file

	if false; then
  	python $borzoi_code_dir"src/scripts/w5_qc.py" -b "$BORZOI_HG38/blacklist/blacklist_hg38_all.bed" -o ${w5_qc_dir}${sample_id} $w5_file
  	fi
done



if false; then
python create_targets_file.py $gtex_bigwig_summary_file $w5_dir $gtex_targets_file
fi