




orig_borzoi_targets_file="${1}"
big_wig_dir="${2}"
gtex_input_bigwig_summary_file="${3}"
gtex_bigwig_summary_file="${4}"
recount3_gtex_bigwig_file_stems="${5}"

source ~/.bashrc
conda activate borzoi



python generate_list_of_gtex_bigwigs_to_download.py $orig_borzoi_targets_file $gtex_input_bigwig_summary_file $recount3_gtex_bigwig_file_stems $gtex_bigwig_summary_file $big_wig_dir


cd $big_wig_dir
tail -n +2 $gtex_input_bigwig_summary_file | while read -r col1 col2 col3 rest; do
    wget "$col3"
done
