# Simple Dimension/Dimension Item checks for ONS API load files

##create_checkfiles.py

Creates .chk files in the relative folder '/CHECK FILES". The .chk files is a pickle written python dictionary containing all the unique dimensions and dimension items present in the source data file.

## compare.py

Lets you compare a flat .csv to the structure outlined in the .chk files created above. If recieving regular data updates, this can be used to validate field and dimension names prior to upload. This allows us to avoid additional, unwanted dimension and sparsity issues resulting from minor undocumented changes in dimension/item labelling in the input files. 


PLEASE NOTE - this is VERY ONS specific at the moment (that might change if I get some time).
