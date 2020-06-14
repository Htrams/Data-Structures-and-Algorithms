import insertion_sort
import binary_insertion_sort
import merge_sort
import max_heap
import binary_search_tree
from timeit import default_timer as timer
from numpy.random import rand

def showOutput(out):
    print(f"\n The sorted Array is {out}")
    return None

def runAlgo(data,algo,name=''):
    start=timer()
    out = algo(data)
    end=timer()
    print('\n\nRunning ' + name + ' Algorithm')
    #showOutput(out)
    print(f'The program took {(end-start)*1000} milli-seconds to complete.\n')
    return None

def heapSort(data):
    return max_heap.MaxHeap(data).heapSort()

def BstSort(data):
    return binary_search_tree.BinarySearchTree().insertArray(data).inOrderTraversal()

print('\n\n*************************************')
print('Welcome to the Sorting Problem.')
print('*************************************\n\n')
print('Choose one of the following options... \n')
print('1. Sort using Insertion Sort (using swaps).')
print('2. Sort using Binary Insertion Sort.')
print('3. Sort using Merge Sort.')
print('4. Sort using Heap Sort.')
print('5. Sort using Binary Search Tree Sort.')

algoOption = int(input('\nYour Choice: '))
if algoOption not in [1,2,3,4,5]:
    print('Wrong Input')
    exit()

inputOption = input('\nGenerate a random unsorted Array? (y/n). ')
if inputOption == 'n' or inputOption == 'N':

    data = input('Please enter an array with numbers. Use commas to separate two numbers. \nFor \
Example - 1,2,3,4,5\n').split(',')
    data = [float(i) for i in data]

elif inputOption == 'y' or inputOption == 'Y':
    arrayDim = int(input("Enter length of unsorted Array to generate. "))
    data=rand(arrayDim).tolist()
    #print(f'\n The following matrix was generated {data}')
else:
    print('Wrong Input.')
    exit()

if algoOption == 1:
    runAlgo(data,insertion_sort.insertionSort,"Insertion Sort")
elif algoOption == 2:
    runAlgo(data,binary_insertion_sort.binaryInsertionSort,"Binary Insertion Sort")
elif algoOption == 3:
    runAlgo(data,merge_sort.mergeSort,"Merge Sort")
elif algoOption == 4:
    runAlgo(data,heapSort,"Heap Sort")
elif algoOption == 5:
    runAlgo(data,BstSort,"Binary Search Tree Sort")