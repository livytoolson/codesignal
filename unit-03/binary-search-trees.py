"""
How can you compute the total number of nodes in a "perfect" binary tree if you know the height?
- 2 ^ h - 1 where h is the height of the binary tree

What is one of the primary weaknesses of the binary search tree as a data structure?
- The performace degrades if it becomes unbalanced

What does the phrase "in-order successor" mean when we are talking about a node in a binary search tree?
- The ndoe that has the next highest value
"""

"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
    
    
def balancedBinaryTree(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if (abs(left_height - right_height) <= 1) and balancedBinaryTree( 
    root.left) is True and balancedBinaryTree(root.right) is True:
        return True
    
    return False


"""
You are given a binary tree and you are asked to write a function that finds its minimum depth. The minimum depth can be defined as the number of nodes along the shortest path from the root down to the nearest leaf node. As a reminder, a leaf node is a node with no children.

Example:
Given the binary tree [5,7,22,None,None,17,9],

    5
   / \
  7  22
    /  \
   17   9
your function should return its minimum depth = 2.
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):
    # Base case: if root is none, depth is 0
    if root is None:
        return 0
    
    # Base case: if root.right and root.left is none, depth is 1
    if root.right is None and root.left is None:
        return 1
    
    # If root.left is none, return min depth of right
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    
    # if root.right is none, return mind depth of left
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
    
    # if left and right are not none, compare left and right and return min 
    left_depth = minimumDepthBinaryTree(root.left)
    right_depth = minimumDepthBinaryTree(root.right)
    
    return min(left_depth, right_depth) + 1


