import numpy as np
import os
import sys
import pdb
import gzip







######################
# Command line args
######################
orig_borzoi_targets_file = sys.argv[1]
gtex_bigwig_summary_file = sys.argv[2]
recount3_gtex_bigwig_file_stems = sys.argv[3]
gtex_bigwig_summary_file2 = sys.argv[4]
big_wig_dir = sys.argv[5]

# First create mapping from gtex sample id to big wig file suffix
mapping = {}
f = open(recount3_gtex_bigwig_file_stems)
for line in f:
	line = line.rstrip()
	line = line[1:]
	sample_id = line.split('.')[2].split('_')[-1]
	if sample_id in mapping:
		print('assumption erororor')
		pdb.set_trace()
	if line.endswith('-1.ALL.bw'):
		new_line = line.split('-1.ALL.b')[0] + '.1.ALL.bw'
	elif line.endswith('-2.ALL.bw'):
		new_line = line.split('-2.ALL.b')[0] + '.2.ALL.bw'
	elif line.endswith('-3.ALL.bw'):
		new_line = line.split('-3.ALL.b')[0] + '.3.ALL.bw'
	elif line.endswith('-4.ALL.bw'):
		new_line = line.split('-4.ALL.b')[0] + '.4.ALL.bw'
	else:
		print('assumptioneroror')
		pdb.set_trace()
	mapping[sample_id] = new_line
f.close()



f = gzip.open(orig_borzoi_targets_file)
t = open(gtex_bigwig_summary_file,'w')
t2 = open(gtex_bigwig_summary_file2,'w')
head_count = 0
for line in f:
	line = line.rstrip().decode('utf-8')
	data = line.split('\t')
	if head_count == 0:
		head_count = head_count + 1
		t.write(line + '\n')
		t2.write(line + '\n')
		continue
	if len(data) != 9:
		print('assumption eroror')
		pdb.set_trace()
	sample_name_full = data[1]
	if sample_name_full.startswith('GTEX') == False:
		continue
	if sample_name_full.endswith('.1') == False:
		print('assumtpioneroror')
		pdb.set_trace()
	sample_name_info = sample_name_full.split('.')
	if len(sample_name_info) != 2:
		print('assumptioner oror')
		pdb.set_trace()

	sample_bigwig = 'https://data.idies.jhu.edu/recount3/data/human/data_sources/gtex/base_sums' + mapping[sample_name_info[0] + '-' + sample_name_info[1]]
	t.write(data[0] + '\t' + data[1] + '\t' + sample_bigwig + '\t' + '\t'.join(data[3:]) + '\n')

	sample_bigwig2 = big_wig_dir + mapping[sample_name_info[0] + '-' + sample_name_info[1]].split('/')[-1]
	t2.write(data[0] + '\t' + data[1] + '\t' + sample_bigwig2 + '\t' + '\t'.join(data[3:]) + '\n')

f.close()
t.close()
t2.close()
