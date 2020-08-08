import counting_sort
import math

def radixSort(data):
    base = 8
    k = max(data)
    digits = math.floor(math.log(k)/math.log(base)) + 1
    for i in range(digits):
        data = counting_sort.countingSort([math.floor(j/base**i) % base for j in data],data)
    return data

print(radixSort([22,24,21,19,26,99,0,3.5,20.5,21.5,23.75]))