# -*- coding: utf-8 -*-
# Created : 2020/5/27 18:54
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn

# this script allows extract seqs by seqs_ID

import argparse as ap
import sys
__version__ = '1.0.0'

def read_params(args):
    p = ap.ArgumentParser(
        description=
        "DESCRIPTION\n"
        "Extract sequences by ID\n"
        "version: " + __version__ + "\n"
        "Detailed introducion \n"
        "Usage \n",

        add_help=False)
    arg = p.add_argument

    arg('-i','--idlist',dest='idlist',help="ID list file", type=str, required=True, default=None)
    arg('-o','--outfasta',dest='outfasta',help="output fasta file", default="Extracted_seqs.faa",nargs='?',type=str)
    arg('-s','--seqsfile',dest='seqsfile',help="sequences file", required=True, default=None,type=str)
    arg("-h", "--help", action="help", help="show this help message and exit")
    pars = p.parse_args()
    return pars


# seqfile = "D:\\Project\\20191011-FunGene\\统计处理\\2-进化树和聚类\\ARG_clustered.faa"
# idfile = "D:\\Project\\20191011-FunGene\\统计处理\\2-进化树和聚类\\emb_ID.txt"

def extract_seq(idlist,seqsfile,outfasta):
    query = []
    with open(idlist) as f:
        lines = f.readlines()
        for i in lines:
            query.append(i.rstrip("\n"))


    seqs = {}
    with open(seqsfile) as s:
        lines = s.readlines()
        for i in lines:
            if i.startswith('>'):
                keys = i.lstrip('>').strip()
                seqs[keys] = []
            else:
                seqs[keys].append(i.strip())
    out = open(outfasta,'w')
    for line in query:
        out.write('>' + str(line) + '\n' + str(''.join(seqs[line])) + '\n')
    out.close()

if __name__ == '__main__':
    pars = read_params(sys.argv)
    extract_seq(pars.idlist,pars.seqsfile,pars.outfasta)









