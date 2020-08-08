class Node:

    def __init__(self,value,parent):
        self.value=value
        self.height=0
        self.right=None
        self.left=None
        self.parent=parent

class AVLtree:

    temp=[]

    def __init__(self):
        self.treeSize = 0
        self.root = Node(None,None)

    def rightRotation(self,y):
        yParent=y.parent
        x=y.left
        xRight=x.right
        
        x.parent=yParent
        x.right=y
        y.parent=x
        y.left=xRight
        if(xRight!=None):
            xRight.parent=y

        # Update Heights
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
        x.height = max(self.getHeight(x.left),self.getHeight(x.right)) + 1

        return x

    def leftRotation(self,x):
        xParent=x.parent
        y=x.right
        yLeft=y.left
        
        y.parent=xParent
        y.left=x
        x.parent=y
        x.right=yLeft
        if(yLeft!=None):
            yLeft.parent=x

        # Update Heights
        x.height = max(self.getHeight(x.left),self.getHeight(x.right)) + 1
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1

        return y

    def getHeight(self,node):
        if node==None:
            return -1
        else:
            return node.height

    def getHeaviness(self,node):
        if node==None:
            return 0
        else:
            return self.getHeight(node.right)-self.getHeight(node.left)
    
    def insert(self,element):
        currentParent = self.root

        # Insert the element in the tree
        if currentParent.value == None:
            currentParent.value=element
            return
        while(True):
            if element > currentParent.value:
                if currentParent.right==None:
                    currentParent.right = Node(element,currentParent)
                    break
                else:
                    currentParent=currentParent.right
            elif element < currentParent.value:
                if currentParent.left == None:
                    currentParent.left = Node(element,currentParent)
                    break
                else:
                    currentParent = currentParent.left
            else:
                print('Duplicate values not supported!')
                break

        # Update Height Values and perform rotations
        while currentParent!=None:
            currentParent.height = max(self.getHeight(currentParent.left),self.getHeight(currentParent.right)) + 1
            currentHeaviness = self.getHeaviness(currentParent)
            rightHeaviness = self.getHeaviness(currentParent.right)
            leftHeaviness = self.getHeaviness(currentParent.left)
            
            temp=currentParent.parent
            newNodes=currentParent
            if currentHeaviness==2:
                if rightHeaviness==1:
                    # Right Right
                    newNodes = self.leftRotation(currentParent)

                elif rightHeaviness==-1:
                    # Right Left
                    currentParent.right = self.rightRotation(currentParent.right)
                    newNodes = self.leftRotation(currentParent)
                else:
                    print('Error')
            elif currentHeaviness==-2:
                if leftHeaviness==-1:
                    # Left Left
                    newNodes = self.rightRotation(currentParent)
                elif leftHeaviness==1:
                    # Left Right
                    currentParent.left = self.leftRotation(currentParent.left)
                    newNodes = self.rightRotation(currentParent)
                else:
                    print('Error')
            else:
                pass

            if temp==None:
                self.root=newNodes
            elif temp.right==currentParent:
                temp.right=newNodes
            elif temp.left==currentParent:
                temp.left=newNodes
            else:
                pass

            currentParent=newNodes
            currentParent=currentParent.parent
        
        return self

    def insertArray(self,elements):
        for i in elements:
            self.insert(i)
        return self

    def inOrderTraversal(self,parent=None):
        if parent==None:
            parent=self.root
            AVLtree.temp=[]

        if parent.left != None:
            # Print left subtree
            self.inOrderTraversal(parent.left)

        # Print root element
        AVLtree.temp.append(parent.value)

        # Print right subtree
        if parent.right != None:
            self.inOrderTraversal(parent.right)
        return AVLtree.temp

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

avlTree = AVLtree()
avlTree.insertArray([50,75,25,87,62,37,13,23,24,1,4,6,8,9,53,56,58,35])
avlTree.printTree()
print(avlTree.inOrderTraversal())