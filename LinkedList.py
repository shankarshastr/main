class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

head = Node(1)

def createLL(temp,val):
    if temp.right == None:
         tempNode = Node(val)
         temp.right = tempNode
         tempNode.left = temp
    else:
        createLL(temp.right,val)

def printLL(temp):
    while temp.right is not None:
        print temp.val
        temp = temp.right

for i in range(2,9):
    createLL(head,i)

printLL(head)

def reverseLL(temp,k):
    count = 0
    while temp.right != None or count!=k:
        count+=1
    if count ==2:
        tempNode = Node(temp.val)
        tempNode.right = temp.right
        tempNode.left = temp.left

        temp.right = tempNode.right
        temp.left = tempNode.left
