# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #get the path from root to p
        stack = []
        stack.append(root)
        path_p = []
        path_q = []
        while stack:
            curNode = stack.pop()
            if curNode.val == p.val:
                path_p.append(curNode)
                break
            if self.containsNode(curNode, p):
                path_p.append(curNode)
            
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)

        stack.append(root)
        while stack:
            curNode = stack.pop()
            if curNode.val == q.val:
                path_q.append(curNode)
                break
            if self.containsNode(curNode, q):
                path_q.append(curNode)
            
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)

        print(f"path_p is {path_p}")
        print(f"path_q is {path_q}")

        i = 0
        if len(path_p) < len(path_q):
            A, B = path_p, path_q 
        else:
            A, B = path_q, path_p
        while i < len(A):
            if A[i] != B[i]:
                return A[i-1]
            i+=1
        
        return A[-1]


    def containsNode(self, root: TreeNode, p: TreeNode) -> bool:
        if root == None:
            return False
        if root.val == p.val:
            return True
        
        return self.containsNode(root.left, p) or self.containsNode(root.right, p)

        