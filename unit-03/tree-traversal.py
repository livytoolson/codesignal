"""
What are the two primary categories for tree traversals?
- Depth-first
- Breadth-first

Select the three different types of depth-first traversals.
- Inorder
- Preorder
- Postorder

Select the correct ordering of steps for an inorder depth-first traversal.
- Go to the left subtree
- Visit node
- Go to the right subtree

Select the correct ordering of steps for a preorder depth-first traversal.
- Visit node
- Go to the left subtree
- Go to the right subtree

Select the correct ordering of steps for a postorder depth-first traversal.
- Go to the left subtree
- Go to the right subtree
- Visit node

What data structure would you use in order to write an iterative depth-first traversal method?
- Stack
"""

"""
You are given a binary tree. Write a function that returns the binary tree's node values using an in-order traversal.

Example:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

res = []

def binaryTreeInOrderTraversal(root):
    
    if root is None:
        return
    
    if root.left:
       binaryTreeInOrderTraversal(root.left)
    
    # print(root.value)
    res.append(root.value)
    
    if root.right:
        binaryTreeInOrderTraversal(root.right)
    
    return res


"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size 

    def enqueue(self, value):
        self.size += 1
        return self.storage.append(value)

    def dequeue(self): 
        if self.size == 0:
            return

        self.size -= 1
        return self.storage.pop(0)
    
res = []
        
def traverseTree(t):
    q = Queue()
    q.enqueue(t)
    
    while q.size != 0:
        cur = q.dequeue()
        
        if cur is None:
            continue
    
        res.append(cur.value)
        
        if cur.left:
            q.enqueue(cur.left)
        if cur.right:
            q.enqueue(cur.right)
        
    return res


"""
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes in the path respectively (noden representing the leaf).

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def treePaths(t):
    res = []
    
    if t is None:
        return res
    
    if t.left is None and t.right is None:
        res.append(str(t.value))
        
    left_subtree = treePaths(t.left)
    right_subtree = treePaths(t.right)
    full_subtree = left_subtree + right_subtree
    
    for leaf in full_subtree:
        res.append(str(t.value) + "->" + leaf)
    
    return res

