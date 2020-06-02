# This program uses a divide and conquer approach for the 2D Peak Finder problem
from helper_funcs import best2Dnbr

def find2Dpeak_binaryDivide(data):
    #Get number of rows
    datax = len(data)

    #Choose middle column
    mid = datax//2
    
    #Find global maximum
    temp1=range(0,len(data[mid]))
    maxloc=0
    maxval=data[mid][0]
    for element in temp1:
        if data[mid][element]>maxval:
            maxloc=element
            maxval=data[mid][element]

    #Check if it is a 2D peak
    temp2 = best2Dnbr(data,(mid,maxloc))
    if temp2==(mid,maxloc):
        return (data[mid][maxloc],(temp2[0]+1,temp2[1]+1))
    
    #Check left or right of global and eliminate one half
    if temp2[0]==mid+1:
        val,pos = find2Dpeak_binaryDivide(data[mid+1:][:])
        pos=(pos[0]+mid+1,pos[1])
    elif temp2[0]==mid-1:
        val,pos = find2Dpeak_binaryDivide(data[:mid][:])

    return (val,pos)