# This program uses an ascent approach for the 2D Peak Finder problem
from helper_funcs import best2Dnbr

def find2Dpeak_ascent(data):
    loc=(0,0)
    check=best2Dnbr(data,loc)
    while check != loc:
        loc=check
        check=best2Dnbr(data,loc)
    return (data[loc[0]][loc[1]],(loc[0]+1,loc[1]+1))   #Added unity to loc to start indexing from one

