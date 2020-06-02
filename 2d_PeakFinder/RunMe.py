from helper_funcs import get2Dinput,showOutput
from Ascent_Approach import find2Dpeak_ascent
from Binary_Divider_Approach import find2Dpeak_binaryDivide
from timeit import default_timer as timer
from numpy.random import rand
from numpy import round

def runAlgo(data,algo,name=''):
    start=timer()
    val,pos = algo(data)
    end=timer()
    print('\n\nRunning ' + name + ' Algorithm')
    showOutput(val,pos)
    print(f'The program took {(end-start)*1000} milli-seconds to complete.\n')
    
    #pos=(pos[0]-1,pos[1]-1)
    #print(f'{data[pos[0]][pos[1]]}')
    #print(f'{data[pos[0]+1][pos[1]]}')
    #print(f'{data[pos[0]-1][pos[1]]}')
    #print(f'{data[pos[0]][pos[1]+1]}')
    #print(f'{data[pos[0]][pos[1]-1]}')
    return None

print('\n\n*************************************')
print('Welcome to the 2D Peak Finder Problem.')
print('*************************************\n\n')
print('Choose one of the following options... \n')
print('1. Solve for 2D Peak using the Ascent Algorithm.')
print('2. Solve for 2D Peak using the Binary Divider Algorithm.')

algoOption = int(input('\nYour Choice: '))
if algoOption!=1 and algoOption!=2:
    print('Wrong Input')
    exit()

inputOption = input('\nGenerate a random 2D matrix? (y/n). ')
if inputOption == 'n' or inputOption == 'N':
    data = get2Dinput()
elif inputOption == 'y' or inputOption == 'Y':
    matrixdime = [int(i) for i in input('Enter the dimensions of \
the randomly generated matrix. Example - 3,4  ').split(',')]
    data=rand(matrixdime[0],matrixdime[1]).tolist()
    #print(f'\n The following matrix was generated {data}')
else:
    print('Wrong Input.')
    exit()

if algoOption == 1:
    runAlgo(data,find2Dpeak_ascent,"Ascent")
elif algoOption == 2:
    runAlgo(data,find2Dpeak_binaryDivide,"Binary Divider")