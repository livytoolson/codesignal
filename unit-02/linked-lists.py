"""
What are the strengths of a Linked List as a data structure?
- Fast operations at both ends - head and tail
- They can grow and shrink to accomodate the data

What is the primary weakness of a Linked List data structure?
- Costly search operations
"""

"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in strictly increasing order, and an integer value. Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];
For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];
For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
# 
def insertValueIntoSortedLinkedList(l, value):
    node = ListNode(value)
    cur = l
    
    # if linked list is none return node
    if l is None:
        return node
    
    # while the current node is not node
    while cur != None:
        if value < cur.value:
            node.next = cur
            return node
            
        if cur.next == None:
            cur.next = node
            return l
            
        if value > cur.value and value < cur.next.value:
            node.next = cur.next
            cur.next = node
            return l
        cur = cur.next
    return l

"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    head = ListNode(0)
    pointer = head
    
    while True:
        if l1 is None and l2 is None:
            break
        elif l1 is None:
            pointer.next = l2
            break
        elif l2 is None:
            pointer.next = l1
            break
        else:
            smaller_value = 0
            if l1.value < l2.value:
                smaller_value = l1.value
                l1 = l1.next
            else:
                smaller_value = l2.value
                l2 = l2.next
            
            new_node = ListNode(smaller_value)
            pointer.next = new_node
            pointer = pointer.next
        
    return head.next

"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    count = 0
    cur = l
    prev = None
    next_node = None
    new_head = None
    old_head = None
    connector = None
    
    while cur:
        count += 1
        cur = cur.next
    
    loops = count // k
    
    cur = l
    
    for num in range(loops):
        connector = old_head
        old_head = cur
        
        for items in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        if connector is not None:
            connector.next = prev
            
        if new_head is None:
            new_head = prev  
             
        old_head.next = cur
    return new_head

# def reverseNodesInKGroups(l, k):
    
#     if k == 1:
#         return l

#     stack = []
#     current = l

#     while current:

#         cur_node = current

#         for i in range(k):
#             if cur_node:
#                 stack.append(cur_node.value)
#                 cur_node = cur_node.next
#             else:
#                 return l

#         for i in range(k):
#             current.value = stack.pop()
#             current = current.next

#         stack = []

#     return l