# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:45:53 2015

@author:  Mike

Create a checkfile using pickle
"""

import pandas as pd
import sys
import numpy as np
import pickle as pk


"""
Create a dictionary of unique dimensions and dim items from a given csv 
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
# TODO - use sys args!
create_unique_dict('transform-rftnewordersq42015corrected-ConstNOT1-.csv', 'CHECK-NOT1')
create_unique_dict('transform-rftnewordersq42015corrected-ConstNOT234-.csv', 'CHECK-NOT234')
create_unique_dict('transform-rftnewordersq42015corrected-ConstNOT5-.csv', 'CHECK-NOT5')
create_unique_dict('transform-rftnewordersq42015corrected-ConstNOT6-.csv', 'CHECK-NOT6')
