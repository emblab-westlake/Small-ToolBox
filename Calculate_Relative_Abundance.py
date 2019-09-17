# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:39:20 2019

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.wdu.cn


"""

import os
import pandas as pd


def main(inputfile):
    current_dir = os.path.abspath(inputfile)
    writefile = current_dir.split('.')[0] + '-Relative.txt'
    if os.path.basename(inputfile).split('.')[1] == 'txt':
        separator = '\t'
    elif os.path.basename(inputfile).split('.')[1] == 'csv':
        separator = ','
    data = pd.read_csv(inputfile, sep=separator,index_col=0,header=0)
    data = data.loc[~(data==0).all(axis=1), :]
    for columnsname in data.columns:
        data[columnsname] = data[columnsname].map(lambda x: x/sum(data[columnsname]))
    data.to_csv(writefile, sep = '\t')



if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate relative abundance")
    parser.add_argument("-i", dest="inputfile", required=True, help="Taxonomy absolute value files")


    args = parser.parse_args()
    main(args.inputfile)
    
    