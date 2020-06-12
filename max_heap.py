class MaxHeap:

    def __init__(self,elements):
        self.heap = elements
        self.siz = len(elements)
        self.build_max_heap()
    
    def leftChild(self,pos):
        return pos*2+1

    def rightChild(self,pos):
        return pos*2+2
    
    def parent(self,pos):
        return (pos-1)//2
    
    def swap(self,pos1,pos2):
        temp = self.heap[pos1]
        self.heap[pos1]=self.heap[pos2]
        self.heap[pos2]=temp

    def exists(self,pos):
        if pos<self.siz and pos>=0:
            return True
        else:
            return False

    def maxHeapify(self,pos): 
        parent = self.heap[pos]
        if self.exists(self.rightChild(pos)):
            left = self.heap[self.leftChild(pos)]
            right = self.heap[self.rightChild(pos)]
            # Compare with both childs
            if left > parent or right > parent:
                if left > right:
                    self.swap(self.leftChild(pos),pos)
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(self.rightChild(pos),pos)
                    self.maxHeapify(self.rightChild(pos))
        elif self.exists(self.leftChild(pos)):
            left = self.heap[self.leftChild(pos)]
            if left > parent:
            # Compare with left child
                self.swap(self.leftChild(pos),pos)
                self.maxHeapify(self.leftChild(pos))
        return None
    
    def build_max_heap(self):
        for i in range((self.siz-2)//2,-1,-1):
            self.maxHeapify(i)

    def heapSort(self):
        '''
        heapSort() messes up the max-heap property. Call build_max_heap() after heapSort() to restore rep-invariant.
        '''

        sortedArray = []
        temp=self.siz
        for i in range(0,self.siz):
            self.swap(0,self.siz-1)
            sortedArray.append(self.heap[self.siz-1])
            self.siz=self.siz-1
            self.maxHeapify(0)
        self.siz = temp
        return sortedArray

    def printHeap(self):
        for i in range(0,(len(self.heap)-2)//2 + 1):
            left = self.heap[self.leftChild(i)] if self.exists(self.leftChild(i)) else None
            right = self.heap[self.rightChild(i)] if self.exists(self.rightChild(i)) else None
            parent = self.heap[i]
            print(f" Parent : {parent} , Left Child : {left} , Right Child : {right}")