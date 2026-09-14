# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue = deque()
        p_queue.append(p)

        q_queue = deque()
        q_queue.append(q)

        while p_queue:
            node1 = p_queue.popleft()
            node2 = q_queue.popleft()
            if node1 == None and node2 == None:
                continue

            if (node1 == None and node2 != None) or (node1 != None and node2 == None):
                return False
    
            if node1.val != node2.val:
                return False
            
            if node1.left:
                p_queue.append(node1.left)
            else:
                if node1.right:
                    p_queue.append(None)

            if node1.right:
                p_queue.append(node1.right)
            else:
                if node1.left:
                    p_queue.append(None)

            if node2.left:
                q_queue.append(node2.left)
            else:
                if node2.right:
                    q_queue.append(None)

            if node2.right:
                q_queue.append(node2.right)
            else:
                if node2.left:
                    q_queue.append(None)
        
        if q_queue:
            return False
        return True


        