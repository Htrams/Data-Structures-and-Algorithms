# This program uses a Binary Search approach for the Peak Finder problem

def findpeak_binary(data):
    siz = len(data)

    #Base case for recurssion
    if siz==1:
        return (data[0],1)
    
    #Get middle element of array
    mid = siz//2

    #Compare the adjacent elements
    if data[mid]<data[mid-1]:
        val,pos=findpeak_binary(data[:mid])
    elif siz!=2 and data[mid]<data[mid+1]:
        val,pos=findpeak_binary(data[mid+1:])
        pos=pos+mid+1
    else:
        val,pos = data[mid],mid+1
    
    #Returning from the function
    return (val,pos)

#Get the 1D array as input
data = input('Enter a 1D array with numbers. ').split(' ')
data = [float(i) for i in data]
val,pos = findpeak_binary(data)
if (val*10)%10==0:
    val=int(val)
print(f'A peak {val} was found at position {pos}. ')