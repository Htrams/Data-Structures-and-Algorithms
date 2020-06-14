class Node:

    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinarySearchTree:

    temp = []

    def __init__(self):
        self.root = Node(None)
        self.size = 0

    def insert(self,element):
        parent = self.root

        # Check if the tree is empty
        if parent.value == None:
            parent.value=element
            self.size = 1
            return self
        
        while(True):
            if element > parent.value:
                if parent.right==None:
                    parent.right = Node(element)
                    self.size = self.size + 1
                    break
                else:
                    parent=parent.right
            elif element < parent.value:
                if parent.left == None:
                    parent.left = Node(element)
                    self.size = self.size + 1
                    break
                else:
                    parent = parent.left
            else:
                print('Duplicate values not supported!')
                break
        return self
    
    def insertArray(self,elements):
        for i in elements:
            self.insert(i)
        return self
    
    def inOrderTraversal(self,parent=None):
        if parent==None:
            parent=self.root
            BinarySearchTree.temp=[]

        if parent.left != None:
            # Print left subtree
            self.inOrderTraversal(parent.left)

        # Print root element
        BinarySearchTree.temp.append(parent.value)

        # Print right subtree
        if parent.right != None:
            self.inOrderTraversal(parent.right)
        return BinarySearchTree.temp
    
    def printTree(self,parent=None):

        if parent==None:
            parent=self.root

        print(f'PARENT: {parent.value}  ,  ' , end='')
        if parent.left != None:
            print(f'LEFT: {parent.left.value}  ,  ' , end='')
        else:
            print(f'LEFT: {None}  ,  ' , end='')
        
        if parent.right != None:
            print(f'RIGHT: {parent.right.value}')
        else:
            print(f'RIGHT: {None}')

        if parent.left != None:
            self.printTree(parent.left)
        if parent.right != None:
            self.printTree(parent.right)

# obj = BinarySearchTree()
# obj.insertArray([50,25,13,37,75,63,87])
# print(obj.inOrderTraversal())
# obj.insert(99)
# print(obj.inOrderTraversal())