# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = []
        stack.append(root)
        while stack:
            curNode = stack.pop()
            if self.sameTree(curNode, subRoot):
                return True
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
        return False
    
    def sameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode])-> bool:
        if tree1 == None and tree2 == None:
            return True

        if (tree1 == None and tree2 != None) or (tree1 != None and tree2 == None):
            return False
        
        if tree1.val != tree2.val:
            return False
            
        if not self.sameTree(tree1.left, tree2.left):
            return False
        if not self.sameTree(tree1.right, tree2.right):
            return False
        
        return True
    
        