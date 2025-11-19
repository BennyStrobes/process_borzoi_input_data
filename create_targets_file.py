import numpy as np
import os
import sys
import pdb








gtex_bigwig_summary_file = sys.argv[1]
w5_dir = sys.argv[2]
gtex_targets_file = sys.argv[3]

head_count = 0
f = open(gtex_bigwig_summary_file)
t = open(gtex_targets_file,'w')
for line in f:
	line = line.rstrip()
	data = line.split('\t')
	if head_count == 0:
		head_count = head_count + 1
		t.write(line + '\n')
		continue
	sample_id = data[1]
	w5_file = w5_dir + sample_id + '.w5'
	t.write(data[0] + '\t' + data[1] + '\t' + w5_file + '\t' + '\t'.join(data[3:]) + '\n')
f.close()
t.close()

print(gtex_targets_file)