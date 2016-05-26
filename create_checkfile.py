# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:45:53 2015

@author:  Mike

Create a checkfile using pickle

"""

import pandas as pd
import sys
import pickle as pk


"""
Create a dictionary of unique dimensions and dim items from a given WDA style flat csv file 
"""
def create_unique_dict(load_file, name):
    my_uniques = []
    obs_file = pd.read_csv(load_file)
    obs_file.fillna('', inplace = True)
    all_cols = list(obs_file.columns.values)
    wanted_cols = []
    for each in all_cols:
        if 'dim_item_id_' in each:
            wanted_cols.append(each)
    for each in all_cols:
        if 'dim_id_' in each:
            wanted_cols.append(each)
    for each in wanted_cols:
        my_uniques.append(pd.unique(obs_file[each].ravel()))
    big_dict = dict(zip(wanted_cols, my_uniques))
    pk.dump(big_dict, open(name + '.chk', 'wb'))


# Put the source files in here
load_file = sys.argv[1]
create_unique_dict(load_file, 'CHECK-' + load_file[:-4])
