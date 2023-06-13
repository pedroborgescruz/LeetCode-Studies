"""
Problem 1: Remove Duplicates from Sorted List
"""

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def removeduplicates(LinkedList):
  """
  Given the head of a sorted linked list, delete all duplicates such that each element appears only          once.   
  Return the linked list sorted as well.
  """
  if (LinkedList == None):
    return None
  
  # Temp node to keep track of start of LinkedList
  temp = LinkedList
  left = LinkedList
  right = LinkedList.next
  
  # While we have nodes in LinkedList, keep checking for duplicates
  while (right is not None):
    # Keep moving right pointer until we find a distinct element compared to data of left pointer
    if (left.data == right.data):
      right = right.next
      if (right == None):
        # Edge case: if all elements are equal, relink to nullpointer; 
        #   check test3()
        left.next = None
        
    else:
      # Reconnect chain and move pointers to start traversing at the same point again
      left.next = right
      left = left.next
      right = right.next

  return temp

def printll(head):
  """
  Print nodes of a LinkedList.
  """
  while head:
    print(head.data)
    head = head.next

def test1():
  print("Test 1:\n")
  head = Node(0)
  ll1 = Node(1)
  ll2 = Node(1)
  ll3 = Node(3)
  ll4 = Node(3)
  ll5 = Node(5) 
  
  head.next = ll1
  ll1.next = ll2
  ll2.next = ll3
  ll3.next = ll4
  ll4.next = ll5
  
  removeduplicate = removeduplicates(head)
  
  printll(removeduplicate)
  print()

def test2():
  print("Test 2:\n")
  head = Node(0)
  ll1 = Node(1)
  ll2 = Node(2)
  ll3 = Node(3)
  ll4 = Node(4)
  ll5 = Node(5) 
  
  head.next = ll1
  ll1.next = ll2
  ll2.next = ll3
  ll3.next = ll4
  ll4.next = ll5
  
  removeduplicate = removeduplicates(head)
  
  printll(removeduplicate)
  print()

def test3():
  print("Test 3:\n")
  head = Node(1)
  ll1 = Node(1)
  ll2 = Node(1)
  ll3 = Node(1)
  ll4 = Node(1)
  ll5 = Node(1) 
  
  head.next = ll1
  ll1.next = ll2
  ll2.next = ll3
  ll3.next = ll4
  ll4.next = ll5
  
  removeduplicate = removeduplicates(head)
  
  printll(removeduplicate)
  print()

def test4():
  print("Test 4:\n")

  removeduplicate = removeduplicates(None)
  
  printll(removeduplicate)
  print()

test1()
test2()
test3()
test4()
