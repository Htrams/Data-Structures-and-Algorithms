
def binaryInsertionSort(data):
    siz = len(data)
    if siz<=1:
        return data
    for i in range(1,siz):
        insertionPlace = binarySearch(data[0:i],data[i])

        #Insert the ith element at the right place
        data = data[0:insertionPlace]+[data[i]]+data[insertionPlace:i]+data[i+1:]

    return data

def binarySearch(data,val):
    siz = len(data)

    #Base Case
    if siz==1:
        if data[0]>val:
            return 0
        else:
            return 1
    if siz==0:
        return 0
    
    #check center element
    mid=siz//2

    if data[mid] < val:
        #Right Halve
        index = mid + binarySearch(data[mid+1:],val) + 1

    else:
        #Left Halve
        index = binarySearch(data[:mid],val)
    
    return index