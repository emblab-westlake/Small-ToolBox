# -*- coding: utf-8 -*-
"""

@author: yuanling

"""
# Usage:
# python3 seqs_length.py FILE.fasta

import sys
lib_file = sys.argv[1]

lib = open(lib_file)
seqs = {} 
for line in lib:
    if '>' in line:
        ORF = line.strip().split(' ')[0].replace('>','')
        seqs[ORF] = []
    else:
        seqs[ORF].append(line.strip())
lib.close()
print('seqs saved!')

seqs_length = {}
for seq in seqs.keys():
    length = 0
    for row in seqs[seq]:
        length += len(row)
    seqs_length[seq] = length
print('seqs length saved!' + '\n')

r = open(''.join(lib_file.split('.')[:-1]) + '.seqs.length.txt','w')
for seq in seqs_length.keys():
    r.write(seq + '\t')
    r.write(str(seqs_length[seq])+'\n')
r.close()