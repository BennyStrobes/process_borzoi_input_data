##############
# Input data
##############
orig_borzoi_targets_file="/home/ch271704/tools/borzoi/data/targets_human.txt.gz"

# Downloaded from https://data.idies.jhu.edu/recount3/data/human/data_sources/gtex/base_sums/all_bws on 11/18/25
recount3_gtex_bigwig_file_stems="/lab-share/CHIP-Strober-e2/Public/Borzoi_data/input_data/all_bws"

# Borzoi code
borzoi_code_dir="/home/ch271704/tools/borzoi/"


##############
# Output data
##############
# Directory containing processed big wigs
big_wig_dir="/lab-share/CHIP-Strober-e2/Public/Borzoi_data/bigwigs/"

# Directory containing processed w5s
w5_dir="/lab-share/CHIP-Strober-e2/Public/Borzoi_data/w5/"
w5_qc_dir="/lab-share/CHIP-Strober-e2/Public/Borzoi_data/w5/qc/"




gtex_input_bigwig_summary_file=${big_wig_dir}"gtex_input_bigwigs_summary.txt"
gtex_bigwig_summary_file=${big_wig_dir}"gtex_bigwigs_summary.txt"
if false; then
sh download_gtex_big_wigs.sh $orig_borzoi_targets_file $big_wig_dir $gtex_input_bigwig_summary_file $gtex_bigwig_summary_file $recount3_gtex_bigwig_file_stems
fi


gtex_targets_file=${w5_dir}"gtex_targets.txt"
if false; then
sh covert_big_wigs_to_w5s.sh $gtex_bigwig_summary_file $w5_dir $borzoi_code_dir $w5_qc_dir $gtex_targets_file
fi

