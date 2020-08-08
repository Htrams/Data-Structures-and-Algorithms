def countingSort(keys,data=None):
    if data==None:
        data=keys

    maxKey = max(keys)
    
    counters = [[] for i in range(maxKey+1)]
    
    for pos,key in enumerate(keys):
        counters[key].append(data[pos])

    output=[]
    for i in range(maxKey+1):
        for j in counters[i]:
            output.append(j)
    
    return output

# print(countingSort([6,0,2,4,1],[(1,1),(2,2),(3,3),(4,4),(5,5)]))