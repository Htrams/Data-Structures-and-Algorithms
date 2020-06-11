
def insertionSort(data):
    siz = len(data)
    if siz<=1:
        return data
    for i in range(1,siz):
        for j in range(i-1,-1,-1):
            #check if done
            if data[j]<=data[j+1]:
                break
            
            #swap j with j+1
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp
    return data