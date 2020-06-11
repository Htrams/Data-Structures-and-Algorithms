
def mergeSort(data):
    siz = len(data)
    
    #Base Case
    if siz<=1:
        return data
    
    #Split and recurse
    leftSide = mergeSort(data[0:siz//2])
    rightSide = mergeSort(data[siz//2:siz])

    #Merge
    merged = []
    leftPoint = 0
    rightPoint = 0
    while True:

        if len(leftSide) == leftPoint:
            for rightPoint in range(rightPoint,len(rightSide)):
                merged.append(rightSide[rightPoint])
            break
        elif len(rightSide) == rightPoint:
            for leftPoint in range(leftPoint,len(leftSide)):
                merged.append(leftSide[leftPoint])
            break

        if leftSide[leftPoint] > rightSide[rightPoint]:
            merged.append(rightSide[rightPoint])
            rightPoint=rightPoint+1
        else:
            merged.append(leftSide[leftPoint])
            leftPoint=leftPoint+1
    return merged
