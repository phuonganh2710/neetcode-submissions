# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        d = deque()
        d.append(root)
        res = []
        while len(d)!=0:
            cur = []
            n = len(d)
            for i in range(n):
                node = d.popleft()
                cur.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(cur)
        return res

        