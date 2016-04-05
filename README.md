# Simple Dimenion/Dimension Item checks for ONS API load files

##create_checkfiles.py

Creates .chk files in the relative folder '/CHECK FILES". The .chk files is a pickly written python dictionary of all unique dimensions and dimension items contained in the .csv.

## compare.py

Lets you compare a flat .csv to the structure outlined in the relevant flat file. The purpose here is to get afvance warning of any munite changes in terminology of dimension/item names that would result in unexpected, additional and sparce dimensions in the final dataset.
