# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
       newNode = ListNode(data,self.head)
       self.head = newNode
       self.size+=1
       return True
       
   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

# myList = LinkedList()
# print("Inserting")
# print(myList.addNode(5))
# print(myList.addNode(15))
# print(myList.addNode(25))
# print("Printing")
# myList.printNode()
# print("Size")
# print(myList.getSize())

def linkedLists():

    listSize1 = randon.randint(0,5)
    listSize2 = randon.randint(0,5)

    list1 = LinkedLists()
    list2 = LinkedLists()

    count = 0
    for i,j in max(len(listSize1, listSize2)):        
        
        i = randon.randint(0,9)
        j = randon.randint(0,9)
        
        ev = True
        
        if count ==0:
            while ev:
                if i == 0:
                    i = randon.randint(0,9)
                if j == 0:
                    j = randon.randint(0,9)

                if i>0 and j>0:
                    ev = False
        list1.addNode(i)
        list2.addNode(j)
    
    return [list1, list2]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
    
        currentNode = ListNode()
        headNode = currentNode
        
        while l1 or l2 or carry == 1:
       
            totalSum = 0
            
            totalSum += carry
            if l1:
                totalSum += l1.val 
                l1 = l1.next
            if l2:
                totalSum += l2.val
                l2 = l2.next


            carry = totalSum // 10
            currentNode.val = totalSum % 10

            if carry == 1:
                currentNode.next = ListNode()
                currentNode = currentNode.next

        return headNode
