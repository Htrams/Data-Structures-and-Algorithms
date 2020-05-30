# This program uses a basic linear approach for the Peak Finder problem

def findpeak_linear(data):
    siz=len(data)
    #Check the peak at the end points
    if data[0]>=data[1]:
        return (data[0],1)
    elif data[-1]>=data[-2]:
        return (data[-1],siz)
    else:
        #Find and print the peak in the middle
        for i in range(1,siz):
            if data[i]>=data[i-1] and data[i]>=data[i+1]:
                return (data[i],i+1)
    return None

def printpeak(val,pos):
    if (val*10)%10==0:
        val=int(val)
    print(f'A peak {val} was found at position {pos}. ')

# Run the program with input

#Get input array
data = input('Enter a 1D array with numbers. ').split(' ')
data = [float(i) for i in data]
val,pos = findpeak_linear(data)
printpeak(val,pos)