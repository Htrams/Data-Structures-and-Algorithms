def best2Dnbr(data,loc):
    '''
    Returns the best neighbour of loc in data.
    If there is no best neighbour, then returns loc.
    '''

    datax=len(data)
    # Define the four neighbours
    poslocs = [(loc[0]+1,loc[1]), \
                (loc[0],loc[1]+1), \
                (loc[0]-1,loc[1]), \
                (loc[0],loc[1]-1)]
    temp=loc
    for posloc in poslocs:
        x=posloc[0]
        y=posloc[1]
        if x<0 or y<0 or x>=datax or y>=len(data[x]):
            continue
        if data[loc[0]][loc[1]] < data[x][y]:
            temp=(x,y)
    return temp

def get2Dinput():
    data = input('Please enter a 2D array with numbers. Use space \
to separate two columns and commas to separate two rows. \nFor \
Example - 1 2 3,4 5 6,7 8 9\n').split(',')
    data = [list(map(float,i.split(' '))) for i in data]
    return data

def showOutput(val,pos):
    if (val*10)%10==0:
        val=int(val)
    print(f'A peak {val} was found at position {pos}. ')